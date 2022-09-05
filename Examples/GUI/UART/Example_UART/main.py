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
from UI_design.Ui_example_GUI_UART import Ui_MainWindow 

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
        self.dev = pywpc.USBDAQF1AOD()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize parameters
        self.connect_flag = 0
        self.port = 0

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
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_open.clicked.connect(self.openPortEvent)
        self.ui.btn_close.clicked.connect(self.closePortEvent)

        self.ui.btn_write.clicked.connect(self.writeEvent)
        self.ui.btn_read.clicked.connect(self.readEvent)

    @asyncSlot() 
    async def openPortEvent(self):
       ## Get information from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        baudrate = self.ui.comboBox_baudrate.currentText()
        databit_idx = self.ui.comboBox_databit.currentIndex()
        parity_idx = self.ui.comboBox_parity.currentIndex()
        stopbit_idx = self.ui.comboBox_stopbit.currentIndex()

        port = port_idx + 1 

        ## Open UART port
        status = await self.dev.UART_open(port) 
        if status == 0: print("UART_open: OK")

        ## Change LED status
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.green_led_path))

        ## Set UART port and baudrate
        await self.dev.UART_setBaudRate(port, int(baudrate))

        ## Set UART port and data bit
        await self.dev.UART_setDataBit(port, databit_idx)

        ## Set UART port and parity
        await self.dev.UART_setParity(port, parity_idx)

        ## Set UART port and stop bit
        await self.dev.UART_setNumStopBit(port, stopbit_idx)

    @asyncSlot() 
    async def writeEvent(self):
        ## Get port from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        # Get write data from UI
        write_data = self.ui.lineEdit_write.text()

        ## Set UART port and and write data to device
        status = await self.dev.UART_write(port, write_data)
        if status == 0: print("UART_write: OK")

    @asyncSlot() 
    async def readEvent(self):
        ## Get bytes to read from UI
        read_bytes = self.ui.lineEdit_byteread.text()

        ## Get port from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        ## Set UART port and read bytes
        data = await self.dev.UART_read(port, int(read_bytes)) 
        self.ui.lineEdit_read.setText(str(data))

    @asyncSlot() 
    async def closePortEvent(self):
        ## Get information from UI
        port_idx = self.ui.comboBox_port.currentIndex()
        port = port_idx + 1

        ## Close UART port
        status = await self.dev.UART_close(port)
        if status == 0: print("UART_close: OK")

        ## Change LED status
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.gray_led_path))

    @asyncSlot() 
    async def connectEvent(self):
        # Get IP from UI
        self.IP = self.ui.lineEdit_IP.text()
        try: 
            ## Connect to USB device
            self.dev.connect(self.IP)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))

            ## Change connection flag
            self.connect_flag = 1

        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
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
