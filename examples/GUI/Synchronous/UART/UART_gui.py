##  Example_UART/ main.py
##  This is example for UART with WPC DAQ Device with synchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import sys
import os

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
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.gray_led_path))

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_open.clicked.connect(self.openPortEvent)
        self.ui.btn_close.clicked.connect(self.closePortEvent)

        self.ui.btn_write.clicked.connect(self.writeEvent)
        self.ui.btn_read.clicked.connect(self.readEvent)

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

        # Get write data from GUI
        self.write_data = self.ui.lineEdit_write.text()

        ## Get bytes to read from GUI
        self.read_bytes = self.ui.lineEdit_byteread.text()

        ## Get baudrate from GUI
        self.baudrate = self.ui.comboBox_baudrate.currentText()

        ## Get databit from GUI
        self.databit = self.ui.comboBox_databit.currentIndex()

        ## Get parity from GUI
        self.parity = self.ui.comboBox_parity.currentIndex()

        ## Get stop bit from GUI
        self.stopbit = self.ui.comboBox_stopbit.currentIndex()

    def openPortEvent(self):
        ## Update Param
        self.updateParam()

        ## Open UART port
        status = self.dev.UART_open(self.port)
        print("UART_open status: ", status)

        ## Set UART port and baudrate
        status = self.dev.UART_setBaudRate(self.port, int(self.baudrate))
        print("UART_setBaudRate status: ", status)

        ## Set UART port and data bit
        status = self.dev.UART_setDataBit(self.port, self.databit)
        print("UART_setDataBit status: ", status)

        ## Set UART port and parity
        status = self.dev.UART_setParity(self.port, self.parity)
        print("UART_setParity status: ", status)

        ## Set UART port and stop bit
        status = self.dev.UART_setNumStopBit(self.port, self.stopbit)
        print("UART_setNumStopBit status: ", status)

        ## Change port LED status
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.blue_led_path))

    def writeEvent(self):
        ## Update Param
        self.updateParam()

        ## Set UART port and and write data to device
        status = self.dev.UART_write(self.port, self.write_data)
        print("UART_write status: ", status)

    def readEvent(self):
        ## Update Param
        self.updateParam()

        ## Set UART port and read bytes
        data = self.dev.UART_read(self.port, int(self.read_bytes)) 
        self.ui.lineEdit_read.setText(str(data))

    def closePortEvent(self):
        ## Update Param
        self.updateParam()

        ## Close UART port
        status = self.dev.UART_close(self.port)
        print("UART_close status: ", status)

        ## Change port LED status
        self.ui.lb_ledport.setPixmap(QtGui.QPixmap(self.green_led_path))

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

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    WPC_main_ui = MainWindow()
    WPC_main_ui.show()
    sys.exit(app.exec_())
