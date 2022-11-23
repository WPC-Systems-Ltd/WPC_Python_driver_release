##  Example_I2C/ main.py
##  This is example for I2C with WPC DAQ Device.
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_I2C import Ui_MainWindow

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
        self.ui.btn_write.clicked.connect(self.writeEvent)
        self.ui.btn_read.clicked.connect(self.readEvent)
        self.ui.btn_set.clicked.connect(self.setClockEvent)
    
    def selectHandle(self): 
        handle_idx = int(self.ui.comboBox_handle.currentIndex()) 
        if handle_idx == 0:
            self.dev = pywpc.USBDAQF1D()
        elif handle_idx == 1:
            self.dev = pywpc.USBDAQF1AD()
        elif handle_idx == 2:
            self.dev = pywpc.USBDAQF1TD()
        elif handle_idx == 3:
            self.dev = pywpc.USBDAQF1RD()
        elif handle_idx == 4:
            self.dev = pywpc.USBDAQF1CD()
        elif handle_idx == 5:
            self.dev = pywpc.USBDAQF1AOD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())+1 
 
        ## Get clock rate from GUI
        self.clock_mode = self.ui.comboBox_clockrate.currentIndex()

        ## Get write address (Hex) from GUI
        self.write_addr = int(self.ui.lineEdit_writeAddr.text(), 16)
     
        ## Get write (Hex) from GUI
        data = self.ui.lineEdit_write.text()

        ## Convert string to int list
        self.write_data = self.converStrtoIntList(data)

        ## Get byte to read from GUI 
        self.byte_read = int(self.ui.lineEdit_byteread.text())

        ## Get read address (Hex) from GUI 
        self.read_addr = int(self.ui.lineEdit_readAddr.text(), 16)  

    @asyncSlot() 
    async def setClockEvent(self):
        ## Update Param
        self.updateParam()

        ## Set I2C port and clock rate
        status = await self.dev.I2C_setClockRate_async(self.port, self.clock_mode)
        print("I2C_setClockRate_async status: ", status)

    @asyncSlot() 
    async def writeEvent(self):
        ## Update Param
        self.updateParam()

        ## Set I2C port and write bytes
        status = await self.dev.I2C_write_async(self.port, self.write_addr, self.write_data) 
        print("I2C_write_async status: ", status) 

    @asyncSlot() 
    async def readEvent(self):
        ## Update Param
        self.updateParam()

        ## Set I2C port and read bytes
        data = await self.dev.I2C_read_async(self.port, self.read_addr, self.byte_read) 
        self.ui.lineEdit_read.setText(str(data))

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

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

        ## Open I2C port
        status = await self.dev.I2C_open_async(self.port)
        print("I2C_open_async status: ", status)
    
    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return
        
        ## Update Param
        self.updateParam()

        ## Close I2C port   
        status = await self.dev.I2C_close_async(self.port)
        print("I2C_close_async status: ", status)

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

    def converStrtoIntList(self, str_):
        ## Split string by commas
        write_data_strlist = str_.replace(' ','').split(',')
        
        ## Convert string list to int list
        write_data_int = []
        for item in write_data_strlist:
            write_data_int.append(int(item, 16))
        return write_data_int

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
