##  main.py
##  Example_UART
##
##  Copyright (c) 2022 WPC Systems Ltd.
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

        ## Create device handle
        self.dev = pywpc.USBDAQF1RD()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize parameters
        self.connect_flag = 0
        self.port = 1

        ## Material path
        file_path = os.path.dirname(__file__)
        self.trademark_path = file_path + "\Material\WPC_trademark.jpg" 
        self.blue_led_path = file_path + "\Material\WPC_Led_blue.png"
        self.red_led_path = file_path + "\Material\WPC_Led_red.png"
        self.green_led_path = file_path + "\Material\WPC_Led_green.png"
        self.gray_led_path = file_path + "\Material\WPC_Led_gray.png"

        ## Set trademark & LED path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_set.clicked.connect(self.setEvent)
        self.ui.btn_RTD.clicked.connect(self.RTDEvent)

    @asyncSlot() 
    async def RTDEvent(self): 
        ## Set RTD port to 1 and read RTD in channels
        for i in range(2):
            data = await self.dev.Thermal_readSensor(self.port, i)
            if i == 0:
                self.ui.lineEdit_sensor0.setText(str(data))
            else:
                self.ui.lineEdit_sensor1.setText(str(data))

    @asyncSlot()
    async def setEvent(self):
       ## Get information from UI  
        type_idx = self.ui.comboBox_type.currentIndex() 
        noiserejection_idx = self.ui.comboBox_noiserejection.currentIndex()
        
        ## Set RTD port to 1 and set type
        for i in range(2):
            status = await self.dev.Thermal_setType(self.port, i, type_idx)
            if status == 0: print("setType: OK")   
 
        ## Set RTD port to 1 and noise filter
        for i in range(2):
            status = await self.dev.Thermal_setNoiseFilter(self.port, i, noiserejection_idx)
            if status == 0: print("setNoiseFilter: OK")
  
    @asyncSlot() 
    async def connectEvent(self):
        ## Get serial_number from UI
        serial_number = self.ui.lineEdit_SN.text()
        try: 
            ## Connect to USB device
            self.dev.connect(serial_number)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

            ## Change connection flag
            self.connect_flag = 1
        except pywpc.Error as err:
            print("err: " + str(err))
        
        ## Open RTD port1
        status = await self.dev.Thermal_open(self.port)
        if status == 0: print("Thermal_open: OK")
    @asyncSlot()      

    async def disconnectEvent(self):
        ## Disconnect network device
        self.dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Change connection flag
        self.connect_flag = 0

        ## Close RTD port1
        status = await self.dev.Thermal_close(self.port)
        if status == 0: print("Thermal_close: OK")   

    def closeEvent(self, event):
        ## Disconnect network device
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
