##  Example_get_device_info/ main.py
##  This is an example for getting information with WPC DAQ Device with synchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import sys
import os 

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
        self.ui.btn_deviceInfo.clicked.connect(self.getdeviceinfoEvent)

    def selectHandle(self): 
        handle_idx = int(self.ui.comboBox_handle.currentIndex()) 
        if handle_idx == 0:
            self.dev = pywpc.WifiDAQE3A()
        elif handle_idx == 1:
            self.dev = pywpc.EthanA()
        elif handle_idx == 2:
            self.dev = pywpc.EthanD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()
   
    def connectEvent(self):
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
    
    def disconnectEvent(self):
        if self.connect_flag == 0:
            return

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
    
    def getdeviceinfoEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Get firmware model & version
        driver_info = self.dev.Sys_getDriverInfo()
        model = driver_info[0]
        version = driver_info[-1]
        
        ## Get serial number & RTC Time
        serial_number = self.dev.Sys_getSerialNumber()
        rtc = self.dev.Sys_getRTC()

        ## Get IP & submask & MAC
        ip, submask = self.dev.Sys_getIPAddrAndSubmask() 
        mac = self.dev.Sys_getMACAddr()

        ## Update information in GUI
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

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    sys.exit(app.exec_())