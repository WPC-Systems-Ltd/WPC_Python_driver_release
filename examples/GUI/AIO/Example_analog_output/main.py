##  main.py
##  Example_analog_output
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_AO import Ui_MainWindow 

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
        self.trademark_path = file_path + "\Material\\trademark.jpg" 
        self.blue_led_path = file_path + "\Material\LED_blue.png"
        self.red_led_path = file_path + "\Material\LED_red.png"
        self.green_led_path = file_path + "\Material\LED_green.png"
        self.gray_led_path = file_path + "\Material\LED_gray.png"

        ## Set trademark & LED path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))
        
        ## Define callback events
        fct_list = [self.hrztSlider_cb0, self.hrztSlider_cb1, self.hrztSlider_cb2, self.hrztSlider_cb3, 
                    self.hrztSlider_cb4, self.hrztSlider_cb5, self.hrztSlider_cb6, self.hrztSlider_cb7]

        for i in range(8):
            obj_hrztSlider = getattr(self.ui, 'horizontalSlider%d' %i)
            obj_hrztSlider.setRange(0,10000)
            obj_hrztSlider.setSingleStep(1)
            obj_hrztSlider.valueChanged.connect(fct_list[i])

        self.ui.btn_update.clicked.connect(self.writeAOValue)
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.btn_setall.clicked.connect(self.setLineEditValueEvent)

    def hrztSlider_cb0(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit0.setText(str(scaledValue))
    
    def hrztSlider_cb1(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit1.setText(str(scaledValue))    

    def hrztSlider_cb2(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit2.setText(str(scaledValue))
    
    def hrztSlider_cb3(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit3.setText(str(scaledValue))

    def hrztSlider_cb4(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit4.setText(str(scaledValue))
    
    def hrztSlider_cb5(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit5.setText(str(scaledValue))
    
    def hrztSlider_cb6(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit6.setText(str(scaledValue))
    
    def hrztSlider_cb7(self, value):
        scaledValue = float(value)/DEVIDER
        self.ui.lineEdit7.setText(str(scaledValue))

    @asyncSlot() 
    async def connectEvent(self):
        if self.connect_flag == 0:
            return

        try: 
            ## Get serial number
            serial_num = self.ui.lineEdit_SN.text()

            ## Connect to USB device
            self.dev.connect(serial_num)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
            
            ## Change connection flag
            self.connect_flag = 1
 
            ## Open AO port
            status = await self.dev.AO_open_async(self.port)
            print("AO_open_async status: ", status)

        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        if self.connect_flag == 0:
            return

        ## Close AO port
        status = await self.dev.AO_close_async(self.port) 
        print("AO_close_async status: ", status) 

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
 
    @asyncSlot()    
    async def writeAOValue(self):
        voltage_list = []
        for i in range(8):
            obj_lineEdit = getattr(self.ui, 'lineEdit%d' %i)
            voltage_list.append(float(obj_lineEdit.text()))

        ## Set AO port to 0 and write data simultaneously
        status = await self.dev.AO_writeAllChannels_async(self.port, voltage_list)
        print("AO_writeAllChannels_async status: ", status)

    def setLineEditValueEvent(self):
        voltage = self.ui.lineEdit_setall.text()
        for i in range(8):
            obj_lineEdit = getattr(self.ui, 'lineEdit%d' %i)
            obj_lineEdit.setText(voltage)

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