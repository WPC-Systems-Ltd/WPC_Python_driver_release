from calendar import c
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from UI_design.Ui_example_GUI_Get_Device_Information import Ui_MainWindow 
from qasync import QEventLoop, asyncSlot
import os
import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  

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

        ## Set tademark path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        
        ## Initialize param
        self.connect_flag = 0
        
        ## Define button callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.btn_deviceInfo.clicked.connect(self.getdeviceinfoEvent)

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')
        
    @asyncSlot()      
    async def connectEvent(self):
        ## Clear error message
        self.clearErrorStatus()

        # Get ip from UI
        self.ip = self.ui.lineEdit_ipConnect.text()
        try: 
            ## Connect to network device
            dev.connect(self.ip)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.blue_led_path))
           
            ## Change connection flag
            self.connect_flag = 1
        except pywpc.Error as err:
            self.ui.lb_err.setText(str(err)) 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## Disconnect network device
        dev.disconnect() 

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
       
        ## Change connection flag
        self.connect_flag = 0

    def closeEvent(self, event):
        ## Disconnect network device
        dev.disconnect()
        
        ## Release device handle
        dev.close()

    @asyncSlot()      
    async def getdeviceinfoEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Clear error message
        self.clearErrorStatus()

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        model = driver_info[0]
        version = driver_info[-1]
        
        ## Get serial number & RTC Time
        serial_number = await dev.Sys_getSerialNumber()
        rtc = await dev.Sys_getRTC()

        ## Get IP & submask & MAC
        ip, submask = await dev.Sys_getIPAddrAndSubmask() 
        mac = await dev.Sys_getMACAddr()

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

    def clearErrorStatus(self):
        self.ui.lb_err.clear()

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
