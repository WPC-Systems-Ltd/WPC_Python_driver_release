##  main.py
##  Example_SPI
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_SPI import Ui_MainWindow 

## WPC
from wpcsys import pywpc

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
        ## Open SPI port
        for i in range(1,3):
            await self.dev.SPI_open(i)

    @asyncSlot()      
    async def closePort(self):
        ## Close SPI port
        for i in range(1,3):
            await self.dev.SPI_close(i)

    @asyncSlot() 
    async def setEvent(self):
        ## Get parameters from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
        mode = self.ui.comboBox_mode.currentIndex()
        prescaler = self.ui.comboBox_prescaler.currentIndex()

        ## Set SPI port and prescaler
        status = await self.dev.SPI_setPrescaler(port, prescaler)
        if status == 0: print("SPI_setPrescaler: OK")
       
        ## Set SPI port and SPI mode
        status = await self.dev.SPI_setMode(port, mode)
        if status == 0: print("SPI_setMode: OK")

    @asyncSlot() 
    async def writeEvent(self):
        ## Get port from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        ## Get write (Hex) from UI
        write_data = self.ui.lineEdit_write.text()

        ## Convert string to int list
        write_data_int = self.converStrtoIntList(write_data)    

        ## Set SPI port and write bytes
        status = await self.dev.SPI_write(port, write_data_int)
        if status == 0: print("SPI_write: OK")

    @asyncSlot() 
    async def readEvent(self):
        ## Get port from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
        
        ## Get write (Hex) from UI
        write_data = self.ui.lineEdit_write.text()

        ## Convert string to int list
        write_data_int = self.converStrtoIntList(write_data)    
 
        ## Set SPI port and read bytes
        data = await self.dev.SPI_readAndWrite(port, write_data_int) 

        ## Update data in UI
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
