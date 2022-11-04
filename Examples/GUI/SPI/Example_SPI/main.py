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

WREN = 0x06
WRITE = 0x02

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Create device handle
        self.dev = pywpc.USBDAQF1TD()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize parameters
        self.connect_flag = 0
        self.DO_port = 0
        self.DO_index = [0] ## CS pin

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
        self.ui.btn_set.clicked.connect(self.setEvent)

    @asyncSlot() 
    async def setEvent(self): 
        ## Get port
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        ## Get mode
        mode = self.ui.comboBox_mode.currentIndex()

        ## Get prescaler
        prescaler = self.ui.comboBox_prescaler.currentIndex()

        ## Set SPI port and prescaler
        status = await self.dev.SPI_setPrescaler_async(port, prescaler)
        print("SPI_setPrescaler_async status: ", status)
       
        ## Set SPI port and SPI mode
        status = await self.dev.SPI_setMode_async(port, mode) 
        print("SPI_setMode_async status: ", status)

    @asyncSlot() 
    async def writeEvent(self):
        ## Get port
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        ## Get write (Hex) from UI
        write_data = self.ui.lineEdit_write.text()

        ## Convert string to int list
        write_data_int = self.converStrtoIntList(write_data)  

        ## Set CS(pin0) to low
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [0])
        print("DO_writePins_async status: ", status)

        ## Write WREN byte
        status = await self.dev.SPI_write_async(port, [WREN])
        print("SPI_write_async status: ", status)

        ## Set CS(pin0) to high
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [1])
        print("DO_writePins_async status: ", status)
  
        ## Set CS(pin0) to low
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [0])
        print("DO_writePins_async status: ", status)

        ## Set SPI port and write bytes
        status = await self.dev.SPI_write_async(port, write_data_int)
        print("SPI_write_async status: ", status)
 
        ## Set CS(pin0) to high
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [1])
        print("DO_writePins_async status: ", status)
 
    @asyncSlot() 
    async def readEvent(self):
        ## Get port from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1
         
        ## Set CS(pin0) to low
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [0])
        print("DO_writePins_async status: ", status)
 
        ## Set SPI port and read bytes 
        write_data = self.ui.lineEdit_write.text()
        write_data_int = self.converStrtoIntList(write_data)
        data = await self.dev.SPI_readAndWrite_async(port, write_data_int) 
        data = ['{:02x}'.format(value) for value in data]
        print("read data :", data) 

        ## Update data in UI
        self.ui.lineEdit_read.setText(str(data))

        ## Set CS(pin0) to high
        status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [1])
        print("DO_writePins_async status: ", status)

        ## Set SPI port and read bytes
        data = await self.dev.SPI_readAndWrite_async(port, write_data_int) 

        ## Update data in UI
        self.ui.lineEdit_read.setText(str(data))

    @asyncSlot() 
    async def connectEvent(self):
        if self.connect_flag == 1:
            return
 
        try: 
            ## Get serial_number from UI
            serial_num = self.ui.lineEdit_SN.text()

            ## Connect to USB device
            self.dev.connect(serial_num)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

            ## Change connection flag
            self.connect_flag = 1

            ## Get port
            port_index = self.ui.comboBox_port.currentIndex()
            print("port_index", port_index)
            port = port_index +1

            ## Open pin0 with digital output
            status = await self.dev.DO_openPins_async(self.DO_port, self.DO_index)
            print("DO_openPins_async status: ", status)
 
            ## Open SPI
            status = await self.dev.SPI_open_async(port)
            print("SPI_open_async status: ", status)

            ## Set CS(pin0) to high
            status = await self.dev.DO_writePins_async(self.DO_port, self.DO_index, [1])
            print("DO_writePins_async status: ", status)
        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return
            
        ## Get port
        port_index = self.ui.comboBox_port.currentIndex() 
        port = port_index +1

        ## Close SPI port
        status = await self.dev.SPI_close_async(port)
        print("SPI_close_async status: ", status)
       
        ## Close pin0 with digital output
        status = await self.dev.DO_closePins_async(self.DO_port, self.DO_index)
        print("DO_closePins_async status: ", status)

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
