##  Example_digital_output/ main.py 
##  This is example for digital output with WPC DAQ Device with asynchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from UI_design.Ui_example_GUI_DO import Ui_MainWindow 

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

        ## Initialize parameters
        self.state_cal = 255
        
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
        self.switch_blue_path = file_path + "\Material\switch_blue.png"
        self.switch_gray_path = file_path + "\Material\switch_gray.png"

        ## Convert backward slash to forward slash
        self.switch_blue_path = self.switch_blue_path.replace('\\', '/')
        self.switch_gray_path = self.switch_gray_path.replace('\\', '/')
 
        ## Set trademark & LED path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))
        
        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        for i in range(8):
            obj_chbox_state = getattr(self.ui, 'checkbox_state%d' %i)
            obj_chbox_state.stateChanged.connect(self.stateDOEvent)
            obj_chbox_state.setStyleSheet("QCheckBox::indicator{ width: 60px;height: 60px;} QCheckBox::indicator:unchecked {image: url("+self.switch_gray_path+");} QCheckBox::indicator:checked {image: url("+self.switch_blue_path+");}")
  
    def selectHandle(self): 
        handle_idx = int(self.ui.comboBox_handle.currentIndex()) 
        if handle_idx == 0:
            self.dev = pywpc.EthanD()
        elif handle_idx == 1:
            self.dev = pywpc.USBDAQF1D()
        elif handle_idx == 2:
            self.dev = pywpc.USBDAQF1DSNK()
        elif handle_idx == 3:
            self.dev = pywpc.USBDAQF1AD()
        elif handle_idx == 4:
            self.dev = pywpc.USBDAQF1TD()
        elif handle_idx == 5:
            self.dev = pywpc.USBDAQF1RD()
        elif handle_idx == 6:
            self.dev = pywpc.USBDAQF1CD()
        elif handle_idx == 7:
            self.dev = pywpc.USBDAQF1AOD()
 
    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())

    @asyncSlot()
    async def stateDOEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Initialize parameter
        self.state_cal = 0

        ## Update Param
        self.updateParam()

        ## Calculate state
        for i in range (8):
            obj_chbox_state = getattr(self.ui, 'checkbox_state%d' % i) 
            state = obj_chbox_state.isChecked()
            self.state_cal += int(state) << i

        ## Write DO state to MCU
        await self.dev.DO_writePort_async(self.port, self.state_cal)

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

        ## Open all DO port
        for i in range(4): 
            status = await self.dev.DO_openPort_async(i) 
            print("DO_openPort_async status: ", status)
            await asyncio.sleep(0.1) ## delay(second)
  
    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Close DO port
        for i in range(4): 
            status = await self.dev.DO_closePort_async(i) 
            print("DO_closePort_async status: ", status)
            await asyncio.sleep(0.1) ## delay(second)
 
        ## Disconnect device
        self.dev.disconnect() 
        
        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))
        
        ## Change connection flag
        self.connect_flag = 0

    def closeEvent(self, event):
        if self.dev is not None:
            ## Disconnect device
            self.dev.disconnect()
            
            ## Release device handle
            self.dev.close()

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
