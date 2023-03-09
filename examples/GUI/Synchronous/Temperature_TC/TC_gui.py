##  Example_Thermo/ main.py
##  This is example for thermocouple with WPC DAQ Device with synchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import sys
import os

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_thermocouple import Ui_MainWindow

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

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)

        self.ui.btn_set.clicked.connect(self.setEvent)
        self.ui.btn_temp.clicked.connect(self.tempEvent)

    def selectHandle(self):
        handle_idx = int(self.ui.comboBox_handle.currentIndex())
        if handle_idx == 0:
            self.dev = pywpc.USBDAQF1TD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())+1

        ## Get type from GUI
        self.type = self.ui.comboBox_type.currentIndex()

        ## Get oversampling from GUI
        self.oversampling = self.ui.comboBox_oversampling.currentIndex()

        ## Get noiserejection from GUI
        self.noiserejection = self.ui.comboBox_noiserejection.currentIndex()

    def tempEvent(self):
        ## Update Param
        self.updateParam()

        ## Read sensor in Channel 0
        data = self.dev.Thermal_readSensor(self.port, 0)
        print("Read channel 0 data:", data, "°C")

        ## Update in GUI
        self.ui.lineEdit_sensor0.setText(str(data))

        ## Read sensor in Channel 1
        data = self.dev.Thermal_readSensor(self.port, 1)
        print("Read channel 1 data:", data, "°C")

        ## Update in GUI
        self.ui.lineEdit_sensor1.setText(str(data))

    def setEvent(self):
        ## Update Param
        self.updateParam()

        ## Set thermo port and type
        for i in range(2):
            status = self.dev.Thermal_setType(self.port, i, self.type)
            print("Thermal_setType status: ", status)

        ## Set thermo port and over-sampling mode
        for i in range(2):
            status = self.dev.Thermal_setOverSampling(self.port, i, self.oversampling)
            print("Thermal_setOverSampling status: ", status)

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

        ## Open thermo port
        status = self.dev.Thermal_open(self.port)
        print("Thermal_open status: ", status)

    def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Update Param
        self.updateParam()

        ## Close thermo port
        status = self.dev.Thermal_close(self.port)
        print("Thermal_close status: ", status)

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