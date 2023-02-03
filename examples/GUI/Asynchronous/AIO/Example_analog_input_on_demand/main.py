##  Example_analog_input_on_demand/ main.py
##  This is example for AI on demand with WPC DAQ Device with asynchronous mode.
##  Copyright (c) 2023 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio
import os
from qasync import QEventLoop, asyncSlot

## Third party
from PyQt5 import QtWidgets, QtGui
from UI_design.Ui_example_GUI_AI_on_demand import Ui_MainWindow 

## WPC
from wpcsys import pywpc

class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

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
 
        ## Get Python driver version
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 
 
        ## Connection flag
        self.connect_flag = 0

        ## Handle declaration
        self.dev = None

        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.btn_onDemand.clicked.connect(self.onDemandEvent)

    def selectHandle(self): 
        handle_idx = int(self.ui.comboBox_handle.currentIndex()) 
        if handle_idx == 0:
            self.dev = pywpc.WifiDAQE3A()
        elif handle_idx == 1:
            self.dev = pywpc.EthanA()
        elif handle_idx == 2:
            self.dev = pywpc.USBDAQF1AD()
        elif handle_idx == 3:
            self.dev = pywpc.USBDAQF1AOD()

    def updateParam(self):
        ## Get IP or serial_number from GUI
        self.ip = self.ui.lineEdit_IP.text()

        ## Get port from GUI
        self.port = int(self.ui.comboBox_port.currentIndex())
  
    @asyncSlot()      
    async def openPort(self):
        ## Update Param
        self.updateParam()

        ## Open AI port
        status = await self.dev.AI_open_async(self.port)
        print("AI_open_async status: ", status)

    @asyncSlot()      
    async def closePort(self):
        ## Update Param
        self.updateParam()

        ## Close AI port
        status = await self.dev.AI_close_async(self.port)
        print("AI_close_async status: ", status)

    @asyncSlot()      
    async def onDemandEvent(self):
        ## Update Param
        self.updateParam()

        ## Set AI port and data acquisition
        data =  await self.dev.AI_readOnDemand_async(self.port)
        if len(data) > 0:
            for i in range(8):
                obj_lineEdit= getattr(self.ui, 'lineEdit_AI%d' %i)
                obj_lineEdit.setText(str(data[i]))

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

        ## Open AI port
        self.openPort()

    @asyncSlot()      
    async def disconnectEvent(self): 
        if self.connect_flag == 0:
            return
        
        ## Close AI port
        self.closePort()

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