##  main.py
##  Example_AI_streaming
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import sys
import os
from qasync import QEventLoop, asyncSlot

## Third party
import matplotlib.animation as animation
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMessageBox
from UI_design.Ui_example_GUI_AIStreaming import Ui_MainWindow 

## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent) 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        ## Material path
        self.trademark_path = os.getcwd() + "\Material\WPC_trademark.jpg" 
        self.blue_led_path = os.getcwd() + "\Material\WPC_Led_blue.png"
        self.red_led_path = os.getcwd() + "\Material\WPC_Led_red.png"
        self.green_led_path = os.getcwd() + "\Material\WPC_Led_green.png"

        ## Set trademark path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))

        ## Get Python driver version
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

        ## Wifi DAQ AI port
        self.AI_port = 1 

        ## Connection flag
        self.connect_flag = 0

        ## Plot parameter
        self.plot_y_min = -10
        self.plot_y_max = 10

        ## AI parameter
        self.ai_sampling_rate = 1000
        self.ai_n_samples = 200
 
        ## List parameter
        self.channel_list = []
        for j in range(8):
            self.channel_list.append([])
        self.plot_total_times = 0

        ## Define button callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent) 
        self.ui.btn_AIStart.clicked.connect(self.startAIEvent)
        self.ui.btn_AIStop.clicked.connect(self.stopAIEvent) 
        self.ui.lineEdit_samplingRate.returnPressed.connect(self.setSamplingRateEvent)
        self.ui.lineEdit_numSamples.returnPressed.connect(self.setNumofSampleEvent) 
        self.ui.comboBox_aiMode.currentIndexChanged.connect(self.chooseAIModeEvent) 
        self.ui.lineEdit_yscaleMax.returnPressed.connect(self.setYscaleMaxEvent)
        self.ui.lineEdit_yscaleMin.returnPressed.connect(self.setYscaleMinEvent)
 
        ## Plotting
        self.plotInitial()
        self.plotAnimation()

        ## Function loop
        self.loop_fct(self.AI_port, 600, 0.005) ## delay [sec]

    def closeEvent(self, event):
        ## Disconnect network device
        dev.disconnect()
        
        ## Release device handle
        dev.close()
 
    @asyncSlot()      
    async def connectEvent(self): 
        # Get ip from UI
        self.ip = self.ui.lineEdit_IP.text()
        try: 
            ## Connect to network device
            dev.connect(self.ip)

            ## Open AI port
            await dev.AI_open(self.AI_port)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))

            ## Change connection flag
            self.connect_flag = 1
        except pywpc.Error as err: 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## close AI port
        await dev.AI_close(self.AI_port)

        ## Disconnect network device
        dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
        
        ## Change connection flag
        self.connect_flag = 0

    @asyncSlot() 
    async def loop_fct(self, port, num_of_sample , delay): 
        while True:
            ## data acquisition
            data = await dev.AI_readStreaming(port, num_of_sample, delay)## Get 600 points at a time 
            if data is not None:
                self.setDisplayPlotNums(data, self.ai_n_samples)
            else: 
                await asyncio.sleep(delay) 

    @asyncSlot()      
    async def startAIEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Get AI mode from UI
        mode = self.ui.comboBox_aiMode.currentIndex()
        
        ## On Demand
        if mode == 0:
            data = await dev.AI_readOnDemand(self.AI_port)
            self.setDisplayPlotNums([data], self.ai_n_samples)
        ## N-Samples/ Continuous 
        else:
            await dev.AI_start(self.AI_port)

    @asyncSlot()      
    async def stopAIEvent(self): 
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return
        await dev.AI_stop(self.AI_port)

    @asyncSlot()
    async def chooseAIModeEvent(self, *args):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return
            
        ## Get AI mode from UI
        mode = int(self.ui.comboBox_aiMode.currentIndex())
        await dev.AI_setMode(self.AI_port, mode)

    @asyncSlot()
    async def setSamplingRateEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        # Get Sampling rate from UI
        sampling_rate = float(self.ui.lineEdit_samplingRate.text())
        self.ai_sampling_rate = sampling_rate
        await dev.AI_setSamplingRate(self.AI_port, sampling_rate)

    @asyncSlot()
    async def setNumofSampleEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        # Get NumSamples from UI
        n_samples = int(self.ui.lineEdit_numSamples.text())
        self.ai_n_samples = n_samples
        await dev.AI_setNumSamples(self.AI_port, n_samples)
      
    def plotInitial(self):
        self.checkboxstatus = [1 for x in range(8)]
        self.matplotlibwidget = MatplotlibWidget()
        for i in range(8):
            self.ui.MplWidget.canvas.axes.plot([0], [0], alpha=self.checkboxstatus[i])

    def plotAnimation(self):
        ## Rearrage x-axis data according to data amount
        self.ani = animation.FuncAnimation(self.ui.MplWidget, self.plotChart, self.plotGetAxisData, interval=100, repeat=True)
        self.ui.MplWidget.canvas.draw()

    def plotGetAxisData(self):
        # Get ch0~ch7 checkbox status from MainUI window
        list_ch = [self.ui.cb_ch0, self.ui.cb_ch1, self.ui.cb_ch2, self.ui.cb_ch3, self.ui.cb_ch4, self.ui.cb_ch5,self.ui.cb_ch6, self.ui.cb_ch7]
        for i in range(8):
            self.checkboxstatus[i] = int(list_ch[i].isChecked())

        # Get xmin, xmax and x list
        m = len(self.channel_list[0])
        x_max = self.plot_total_times
        x_min = max(x_max - m, 0)
        x_list = list(range(x_min, x_max))

        # Get xticks
        if m > 5:
            dx = m // 6
            ticks = np.arange(x_min, x_max, dx)
        else:
            ticks = np.arange(x_min, x_max)
        yield x_list, ticks, x_min, x_max, self.checkboxstatus
 
    def plotChart(self, update):
        # Define update value
        x_list, ticks, x_min, x_max, self.checkboxstatus = update
 
        # Clear all axes info
        self.ui.MplWidget.canvas.axes.clear()
        
        # Plot 8 channels data
        try:
            for i in range(8):
                self.ui.MplWidget.canvas.axes.plot(x_list, self.channel_list[i], alpha=self.checkboxstatus[i],
                                                marker='o', markersize=2)
        except:
            print("err_xlist " + str(len(x_list)))
            print("err_ylist " + str(len(self.channel_list[i])))


        # Set x,y limit
        self.ui.MplWidget.canvas.axes.set_ylim(float(self.plot_y_min) * 1.05, float(self.plot_y_max) * 1.05)
        self.ui.MplWidget.canvas.axes.set_xlim(x_min, x_max)

        # Set xtickslabel
        self.ui.MplWidget.canvas.axes.set_xticks(ticks)
        new_ticks = self.plotConvertXtick(ticks)
        self.ui.MplWidget.canvas.axes.set_xticklabels(new_ticks)

        # Set label
        self.ui.MplWidget.canvas.axes.set_xlabel("Time (s)", fontsize=12)
        self.ui.MplWidget.canvas.axes.set_ylabel("Voltage (V)", fontsize=12)

        # Set legend
        self.ui.MplWidget.canvas.axes.legend(('ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'),
                                            loc='center left', shadow=False, fontsize=10, bbox_to_anchor=(1, 0.75),
                                            facecolor='#f0f0f0')
        # Set grid
        self.ui.MplWidget.canvas.axes.grid(color='#bac3d1', linestyle='-', linewidth=0.8)  # grid

    def plotConvertXtick(self, xtick):
        return ["{:.2f}".format(x / self.ai_sampling_rate) for i, x in enumerate(xtick)]

    def setDisplayPlotNums(self, data, nums):
        data = np.array(data)
        self.plot_total_times += len(data)
        
        # for plotting
        for k in range(8):
            self.channel_list[k].extend(data[:, k])
            self.channel_list[k] = self.channel_list[k][-(nums):]

    def setYscaleMaxEvent(self):
        # Get yscaleMax from MainUI window
        self.plot_y_max = self.ui.lineEdit_yscaleMax.text()

    def setYscaleMinEvent(self):
        # Get yscaleMin from MainUI window
        self.plot_y_min = self.ui.lineEdit_yscaleMin.text()

    def checkConnectionStatus(self):
        if self.connect_flag == 0:
            QMessageBox.information(self, "Error Messages", "Please connect server first.", QMessageBox.Ok)
            return False
        else:
            return True

def main(): 
    app = QtWidgets.QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    with loop: 
        loop.run_forever()

if __name__ == "__main__":
    ## Create device handle
    dev = pywpc.WifiDAQE3A()
    main()