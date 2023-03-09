##  Example_RTD/ main.py
##  This is example for RTD with WPC DAQ Device with asynchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_RTD import Ui_MainWindow

## WPC
from wpcsys import pywpc

DEVIDER = 2000
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Get Python driver version
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Connection flag
        self.connect_flag = 0

        ## Handle declaration
        self.dev = None

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

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_set.clicked.connect(self.setEvent)
        self.ui.btn_RTD.clicked.connect(self.RTDEvent)

    def selectHandle(self):
        handle_idx = int(self.ui.comboBox_handle.currentIndex())
        if handle_idx == 0:
            self.dev = pywpc.USBDAQF1RD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())+1

        ## Get type from GUI
        self.type = self.ui.comboBox_type.currentIndex()

        ## Get noiserejection from GUI
        self.noiserejection = self.ui.comboBox_noiserejection.currentIndex()

    @asyncSlot()
    async def RTDEvent(self):
        ## Update Param
        self.updateParam()

        ## Read sensor in Channel 0
        data = await self.dev.Thermal_readSensor_async(self.port, 0)
        print("Read channel 0 data:", data, "°C")

        ## Update in GUI
        self.ui.lineEdit_sensor0.setText(str(data))

        ## Read sensor in Channel 1
        data = await self.dev.Thermal_readSensor_async(self.port, 1)
        print("Read channel 1 data:", data, "°C")

        ## Update in GUI
        self.ui.lineEdit_sensor1.setText(str(data))

    @asyncSlot()
    async def setEvent(self):
        ## Update Param
        self.updateParam()

        ## Set RTD port to 1 and set type for two channels
        for i in range(2):
            status = await self.dev.Thermal_setType_async(self.port, i, self.type)
            print("Thermal_setType_async status: ", status)

        ## Set RTD port to 1 and noise filter for two channels
        for i in range(2):
            status = await self.dev.Thermal_setNoiseFilter_async(self.port, i, self.noiserejection)
            print("Thermal_setNoiseFilter_async status: ", status)

    @asyncSlot()
    async def connectEvent(self):
        if self.connect_flag == 1:
            return

        ## Select handle
        self.selectHandle()

        ## Update Param
        self.updateParam()

        ## Connect to device
        try:
            self.dev.connect(self.ip)
        except pywpc.Error as err:
            print("err: " + str(err))
            return

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))

        ## Change connection flag
        self.connect_flag = 1

        ## Open RTD port
        status = await self.dev.Thermal_open_async(self.port)
        print("Thermal_open_async status: ", status)

    @asyncSlot()
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Update Param
        self.updateParam()

        ## Close RTD port
        status = await self.dev.Thermal_close_async(self.port)
        print("Thermal_close_async status: ", status)

        ## Disconnect device
        self.dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

        ## Change connection flag
        self.connect_flag = 0

    def closeEvent(self, event):
        if self.dev is not None:
            ## Disconnect device
            self.dev.disconnect()

            ## Release device handle
            self.dev.close()

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
