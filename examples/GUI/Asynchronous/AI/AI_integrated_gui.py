##  Example_analog_input/main.py
##  This is example for AI streaming with WPC DAQ Device with asynchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
import numpy as np
import matplotlib.animation as animation
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

        ## Connection flag
        self.connect_flag = 0

        ## Handle declaration
        self.dev = None

        ## Plot parameter
        self.plot_y_min = -10
        self.plot_y_max = 10

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

    def closeEvent(self, event):
        if self.dev is not None:
            ## Disconnect device
            self.disconnectEvent()
            ## Release device handle
            self.dev.close()
        else:
            self.killed = True

    def selectHandle(self):
        handle_idx = int(self.ui.comboBox_handle.currentIndex())
        if handle_idx == 0:
            self.dev = pywpc.WifiDAQE3A()
        elif handle_idx == 1:
            self.dev = pywpc.EthanA()
        elif handle_idx == 2:
            self.dev = pywpc.USBDAQF1AD()
        elif handle_idx == 3:
            self.dev = pywpc.USBDAQF1AOD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())

        ## Get AI mode from UI
        self.mode = self.ui.comboBox_aiMode.currentIndex()

        ## Get Sampling rate from UI
        self.ai_sampling_rate = float(self.ui.lineEdit_samplingRate.text())

        ## Get NumSamples from UI
        self.ai_n_samples = int(self.ui.lineEdit_numSamples.text())

    @asyncSlot()
    async def connectEvent(self):
        if self.connect_flag == 1:
            return

        ## Select handle
        self.selectHandle()

        ## Update Param
        self.updateParam()

        try:
            ## Connect to device
            self.dev.connect(self.ip)
        except pywpc.Error as err:
            print("err: " + str(err))
            return

        ## Open AI port
        status = await self.dev.AI_open_async(self.port)
        print("AI_open_async status: ", status)

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))

        ## loop start
        self.killed = False
        self.loop_fct()

        ## Change connection flag
        self.connect_flag = 1

    @asyncSlot()
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## close AI port
        status = await self.dev.AI_close_async(self.port)
        print("AI_close_async status: ", status)

        ## Disconnect device
        self.dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

        self.killed = True

        ## Change connection flag
        self.connect_flag = 0

    @asyncSlot()
    async def loop_fct(self):
        while not self.killed:
            ## data acquisition
            data = await self.dev.AI_readStreaming_async(self.port, 600, 0.005)## Get 600 points at a time 
            if len(data) >0 :
                self.setDisplayPlotNums(data, self.ai_n_samples)
            await asyncio.sleep(0.005)

    @asyncSlot()
    async def startAIEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Update Param
        self.updateParam()

        ## On Demand
        if self.mode == 0:
            data = await self.dev.AI_readOnDemand_async(self.port)
            self.setDisplayPlotNums([data], self.ai_n_samples)
        ## N-Samples/Continuous
        else:
            status = await self.dev.AI_start_async(self.port)
            print("AI_start_async status: ", status)

    @asyncSlot()
    async def stopAIEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Update Param
        self.updateParam()

        ## Send AI stop
        status = await self.dev.AI_stop_async(self.port)
        print("AI_stop_async status: ", status)

    @asyncSlot()
    async def chooseAIModeEvent(self, *args):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Update Param
        self.updateParam()

        ## Send AI mode
        status = await self.dev.AI_setMode_async(self.port, self.mode)
        print("AI_setMode_async status: ", status)

    @asyncSlot()
    async def setSamplingRateEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Update Param
        self.updateParam()

        ## Send set sampling rate
        status = await self.dev.AI_setSamplingRate_async(self.port, self.ai_sampling_rate)
        print("AI_setSamplingRate_async status: ", status)

    @asyncSlot()
    async def setNumofSampleEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Update Param
        self.updateParam()

        ## Send set number of samples
        status = await self.dev.AI_setNumSamples_async(self.port, self.ai_n_samples)
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