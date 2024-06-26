##  Example_SPI/ main.py
##  This is example for SPI with WPC DAQ Device with synchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import sys
import os

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
        self.ui.btn_set.clicked.connect(self.setEvent)

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
        ## DO port and pin
        self.DO_port = 0
        self.DO_index = [0] ## CS pin

        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())+1

        ## Get mode from GUI
        self.mode = self.ui.comboBox_mode.currentIndex()

        ## Get prescaler from GUI
        self.prescaler = self.ui.comboBox_prescaler.currentIndex()

        ## Get write (Hex) from GUI
        data = self.ui.lineEdit_write.text()

        ## Convert string to int list
        self.write_data = self.converStrtoIntList(data)

    def setEvent(self):
        ## Update Param
        self.updateParam()

        ## Set SPI port and prescaler
        status = self.dev.SPI_setPrescaler(self.port, self.prescaler)
        print("SPI_setPrescaler status: ", status)

        ## Set SPI port and mode
        status = self.dev.SPI_setMode(self.port, self.mode)
        print("SPI_setMode status: ", status)

    def writeEvent(self):
        ## Update Param
        self.updateParam()

        ## Set CS(pin0) to low
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [0])
        print("DO_writePins status: ", status)

        ## Write WREN byte
        status = self.dev.SPI_write(self.port, [WREN])
        print("SPI_write status: ", status)

        ## Set CS(pin0) to high
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [1])
        print("DO_writePins status: ", status)

        ## Set CS(pin0) to low
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [0])
        print("DO_writePins status: ", status)

        ## Set SPI port and write bytes
        status = self.dev.SPI_write(self.port, self.write_data)
        print("SPI_write status: ", status)

        ## Set CS(pin0) to high
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [1])
        print("DO_writePins status: ", status)

    def readEvent(self):
        ## Update Param
        self.updateParam()

        ## Set CS(pin0) to low
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [0])
        print("DO_writePins status: ", status)

        ## Set SPI port and read bytes
        data = self.dev.SPI_readAndWrite(self.port, self.write_data)
        data = ['{:02x}'.format(value) for value in data]
        print("read data :", data)

        ## Update data in GUI
        self.ui.lineEdit_read.setText(str(data))

        ## Set CS(pin0) to high
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [1])
        print("DO_writePins status: ", status)

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

        ## Open pin0 with digital output
        status = self.dev.DO_openPins(self.DO_port, self.DO_index)
        print("DO_openPins status: ", status)

        ## Open SPI
        status = self.dev.SPI_open(self.port)
        print("SPI_open status: ", status)

        ## Set CS(pin0) to high
        status = self.dev.DO_writePins(self.DO_port, self.DO_index, [1])
        print("DO_writePins status: ", status)

    def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Update Param
        self.updateParam()

        ## Close SPI port
        status = self.dev.SPI_close(self.port)
        print("SPI_close status: ", status)

        ## Close pin0 with digital output
        status = self.dev.DO_closePins(self.DO_port, self.DO_index)
        print("DO_closePins status: ", status)

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

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    WPC_main_ui = MainWindow()
    WPC_main_ui.show()
    sys.exit(app.exec_())