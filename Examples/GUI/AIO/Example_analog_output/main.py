##  main.py
##  Example_analog_output
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
from UI_design.Ui_example_GUI_Analog_Output import Ui_MainWindow 

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
        self.dev = pywpc.USBDAQF1AOD()

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        ## Initialize parameters
        self.connect_flag = 0
        self.port = 0

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
        # Get IP from UI
        self.IP = self.ui.lineEdit_IP.text()
        try: 
            ## Connect to USB device
            self.dev.connect(self.IP)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
            
            ## Change connection flag
            self.connect_flag = 1
 
            ## Open AO port0
            status = await self.dev.AO_open(self.port)
            if status == 0: print("AO_open: OK")

        except pywpc.Error as err:
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## Close AO port0
        status = await self.dev.AO_close(self.port) 
        if status == 0: print("AO_close: OK") 

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
        status = await self.dev.AO_writeAllChannels(self.port, voltage_list)
        if status == 0: print("AO_writeAllChannels: OK")

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
