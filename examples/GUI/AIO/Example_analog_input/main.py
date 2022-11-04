##  main.py
##  Example_analog_input
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
import matplotlib.animation as animation
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMessageBox
from UI_design.Ui_example_GUI_AI import Ui_MainWindow 

## WPC
from wpcsys import pywpc

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
        file_path = os.path.dirname(__file__)
        self.trademark_path = file_path + "\Material\\trademark.jpg" 
        self.blue_led_path = file_path + "\Material\LED_blue.png"
        self.red_led_path = file_path + "\Material\LED_red.png"
        self.green_led_path = file_path + "\Material\LED_green.png"
        self.gray_led_path = file_path + "\Material\LED_gray.png"

        ## Set trademark & LED path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Get Python driver version
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

        ## Create device handle
        self.dev = pywpc.EthanA()
        
        ## AI port
        self.port = 0 

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

        ## Define callback events
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
        self.loop_fct(self.port, 600, 0.005) ## delay [sec]

    def closeEvent(self, event):
        ## Disconnect network device
        self.dev.disconnect()
        
        ## Release device handle
        self.dev.close()
 
    @asyncSlot()      
    async def connectEvent(self): 
        if self.connect_flag == 1:
            return 

        ## Get IP 
        ip = self.ui.lineEdit_IP.text()
        try: 
            ## Connect to device
            self.dev.connect(ip)
        except pywpc.Error as err:
            print(str(err))

        ## Open AI port
        status = await self.dev.AI_open_async(self.port)
        print("AI_open_async status: ", status)

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))

        ## Change connection flag
        self.connect_flag = 1
 
    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return 
   
        ## close AI port
        status = await self.dev.AI_close_async(self.port)
        print("AI_close_async status: ", status)

        ## Disconnect network device
        self.dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
        
        ## Change connection flag
        self.connect_flag = 0

    @asyncSlot() 
    async def loop_fct(self, port, num_of_sample , delay): 
        while True:
            ## data acquisition
            data = await self.dev.AI_readStreaming_async(port, num_of_sample, delay)## Get 600 points at a time 
            if len(data) >0 :
                self.setDisplayPlotNums(data, self.ai_n_samples)
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
            data = await self.dev.AI_readOnDemand_async(self.port) 
            self.setDisplayPlotNums([data], self.ai_n_samples)
        ## N-Samples/ Continuous 
        else:
            status = await self.dev.AI_start_async(self.port)
            print("AI_start_async status: ", status)
    
    @asyncSlot()      
    async def stopAIEvent(self): 
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return
        
        ## Send AI stop
        status = await self.dev.AI_stop_async(self.port)
        print("AI_stop_async status: ", status)

    @asyncSlot()
    async def chooseAIModeEvent(self, *args):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return
            
        ## Get AI mode from UI
        mode = int(self.ui.comboBox_aiMode.currentIndex())

        ## Send AI mode
        status = await self.dev.AI_setMode_async(self.port, mode)
        print("AI_setMode_async status: ", status)
    
    @asyncSlot()
    async def setSamplingRateEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Get Sampling rate from UI
        sampling_rate = float(self.ui.lineEdit_samplingRate.text())
        self.ai_sampling_rate = sampling_rate
        
        ## Send set sampling rate
        status = await self.dev.AI_setSamplingRate_async(self.port, sampling_rate)
        print("AI_setSamplingRate_async status: ", status)

    @asyncSlot()
    async def setNumofSampleEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Get NumSamples from UI
        n_samples = int(self.ui.lineEdit_numSamples.text())
        self.ai_n_samples = n_samples
        
        ## Send set number of samples
        status = await self.dev.AI_setNumSamples_async(self.port, n_samples)
        print("AI_setNumSamples_async status: ", status)

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

        ## Get xmin, xmax and x list
        m = len(self.channel_list[0])
        x_max = self.plot_total_times
        x_min = max(x_max - m, 0)
        x_list = list(range(x_min, x_max))

        ## Get xticks
        if m > 5:
            dx = m // 6
            ticks = np.arange(x_min, x_max, dx)
        else:
            ticks = np.arange(x_min, x_max)
        yield x_list, ticks, x_min, x_max, self.checkboxstatus
 
    def plotChart(self, update):
        ## Define update value
        x_list, ticks, x_min, x_max, self.checkboxstatus = update
 
        ## Clear all axes info
        self.ui.MplWidget.canvas.axes.clear()
        
        ## Plot 8 channels data
        try:
            for i in range(8):
                self.ui.MplWidget.canvas.axes.plot(x_list, self.channel_list[i], alpha=self.checkboxstatus[i],
                                                marker='o', markersize=2)
        except:
            print("err_xlist " + str(len(x_list)))
            print("err_ylist " + str(len(self.channel_list[i])))


        ## Set x,y limit
        self.ui.MplWidget.canvas.axes.set_ylim(float(self.plot_y_min) * 1.05, float(self.plot_y_max) * 1.05)
        self.ui.MplWidget.canvas.axes.set_xlim(x_min, x_max)

        ## Set xtickslabel
        self.ui.MplWidget.canvas.axes.set_xticks(ticks)
        new_ticks = self.plotConvertXtick(ticks)
        self.ui.MplWidget.canvas.axes.set_xticklabels(new_ticks)

        ## Set label
        self.ui.MplWidget.canvas.axes.set_xlabel("Time (s)", fontsize=12)
        self.ui.MplWidget.canvas.axes.set_ylabel("Voltage (V)", fontsize=12)

        ## Set legend
        self.ui.MplWidget.canvas.axes.legend(('ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'),
                                            loc='center left', shadow=False, fontsize=10, bbox_to_anchor=(1, 0.75),
                                            facecolor='#f0f0f0')
        ## Set grid
        self.ui.MplWidget.canvas.axes.grid(color='#bac3d1', linestyle='-', linewidth=0.8)  # grid

    def plotConvertXtick(self, xtick):
        return ["{:.2f}".format(x / self.ai_sampling_rate) for i, x in enumerate(xtick)]

    def setDisplayPlotNums(self, data, nums):
        data = np.array(data)
        self.plot_total_times += len(data)
        ## for plotting
        for k in range(8):
            self.channel_list[k].extend(data[:, k])
            self.channel_list[k] = self.channel_list[k][-(nums):]

    def setYscaleMaxEvent(self):
        ## Get yscaleMax from MainUI window
        self.plot_y_max = self.ui.lineEdit_yscaleMax.text()

    def setYscaleMinEvent(self):
        ## Get yscaleMin from MainUI window
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
    main()