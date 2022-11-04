##  main.py
##  Example_get_device_info
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from UI_design.Ui_example_GUI_get_device_info import Ui_MainWindow 

## WPC
from wpcsys import pywpc

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Create device handle
        self.dev = pywpc.WifiDAQE3A()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize param
        self.connect_flag = 0

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
        self.ui.btn_deviceInfo.clicked.connect(self.getdeviceinfoEvent)

    @asyncSlot()      
    async def connectEvent(self):
        if self.connect_flag == 1:
            return

        # Get IP
        ip = self.ui.lineEdit_ipConnect.text()
        try: 
            ## Connect to network device
            self.dev.connect(ip)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))
           
            ## Change connection flag
            self.connect_flag = 1
        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Disconnect network device
        self.dev.disconnect() 

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
       
        ## Change connection flag
        self.connect_flag = 0

    def closeEvent(self, event):
        ## Disconnect network device
        self.dev.disconnect()
        
        ## Release device handle
        self.dev.close()

    @asyncSlot()      
    async def getdeviceinfoEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Get firmware model & version
        driver_info = await self.dev.Sys_getDriverInfo_async()
        model = driver_info[0]
        version = driver_info[-1]
        
        ## Get serial number & RTC Time
        serial_number = await self.dev.Sys_getSerialNumber_async()
        rtc = await self.dev.Sys_getRTC_async()

        ## Get IP & submask & MAC
        ip, submask = await self.dev.Sys_getIPAddrAndSubmask_async() 
        mac = await self.dev.Sys_getMACAddr_async()

        ## Update information in UI
        self.ui.lineEdit_ip.setText(ip)
        self.ui.lineEdit_sbk.setText(submask)
        self.ui.lineEdit_serialNum.setText(serial_number)
        self.ui.lineEdit_mac.setText(mac)
        self.ui.lineEdit_model.setText(model)
        self.ui.lineEdit_version.setText(version)
        self.ui.lineEdit_rtc.setText(rtc)

    ## Check TCP connection with QMessageBox
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