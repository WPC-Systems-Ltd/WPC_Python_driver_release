##  main.py
##  Example_UART
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import sys
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_I2C import Ui_MainWindow 

## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  


DEVIDER = 2000
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Create device handle
        self.dev = pywpc.USBDAQF1D()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize parameters
        self.connect_flag = 0
    
        ## Material path
        current_folder = os.getcwd().replace('\\', '/')
        self.trademark_path = current_folder + "/Material/WPC_trademark.jpg"  
        self.gray_led_path = current_folder + "/Material/WPC_Led_gray.png"
        self.green_led_path = current_folder + "/Material/WPC_Led_green.png"
        self.switch_gray_path = current_folder + "/Material/switch_gray.png"
        self.switch_blue_path = current_folder + "/Material/switch_blue.png" 

        ## Set trademark & LED path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_write.clicked.connect(self.writeEvent)
        self.ui.btn_read.clicked.connect(self.readEvent)
        self.ui.btn_set.clicked.connect(self.setEvent)


    @asyncSlot()      
    async def openPort(self):
        ## Open I2C port
        for i in range(1,3):
            await self.dev.I2C_open(i)

    @asyncSlot()      
    async def closePort(self):
        ## Close I2C port
        for i in range(1,3):
            await self.dev.I2C_close(i)

    @asyncSlot() 
    async def setEvent(self):
        ## Get parameters from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
        clock_mode = self.ui.comboBox_clockrate.currentIndex()

        ## Set I2C port and clock rate
        status = await self.dev.I2C_setClockRate(port, clock_mode)
        if status == 0: print("SPI_setPrescaler: OK")

    @asyncSlot() 
    async def writeEvent(self):
        ## Get information from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
        read_addr = self.ui.lineEdit_writeAddr.text()

        ## Get write data from UI
        write_data = self.ui.lineEdit_write.text()
        
        ## Set I2C port and write bytes
        status = await self.dev.I2C_write(port, int(read_addr),  int(write_data))
        if status == 0: print("I2C_write: OK")

    @asyncSlot() 
    async def readEvent(self):
        ## Get information from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
        byte_read = self.ui.lineEdit_byteread.text()
        read_addr = self.ui.lineEdit_readAddr.text()

        ## Set I2C port and read bytes
        data = await self.dev.I2C_read(port, int(read_addr), int(byte_read)) 
        self.ui.lineEdit_read.setText(str(data))

    @asyncSlot() 
    async def connectEvent(self):
        # Get serial_number from UI
        serial_num = self.ui.lineEdit_SN.text()
        try: 
            ## Connect to USB device
            self.dev.connect(serial_num)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

            ## Change connection flag
            self.connect_flag = 1

            ## Open SPI port
            self.openPort()

        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## Close SPI port
        self.closePort()

        ## Disconnect network device
        self.dev.disconnect()

        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Change connection flag
        self.connect_flag = 0
        
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
