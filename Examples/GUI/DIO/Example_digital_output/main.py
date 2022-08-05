from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from UI_design.Ui_example_GUI_Digital_Output import Ui_MainWindow 
from qasync import QEventLoop, asyncSlot
import os
import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Parameters
        self.enable_cal = 255
        self.state_cal = 255

        ## Material path
        current_folder = os.getcwd().replace('\\', '/')
        self.trademark_path = current_folder + "/Material/WPC_trademark.jpg"  
        self.gray_led_path = current_folder + "/Material/WPC_Led_gray.png"
        self.green_led_path = current_folder + "/Material/WPC_Led_green.png"
        self.switch_gray_path = current_folder + "/Material/switch_gray.png"
        self.switch_blue_path = current_folder + "/Material/switch_blue.png" 

        ## Set trademark path
        self.ui.lb_trademark.setPixmap(QtGui.QPixmap(self.trademark_path))

        ## Set led path
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))
        
        ## Initialize param
        self.connect_flag = 0
        
        ## Define callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.combobox_port.currentIndexChanged.connect(self.portEvent)

        for i in range(0, 8):
            obj_chbox_state = getattr(self.ui, 'cb_state%d' %i) 
            obj_chbox_state.stateChanged.connect(self.stateDOEvent)
            obj_chbox_state.setStyleSheet("QCheckBox::indicator{ width: 60px;height: 60px;} QCheckBox::indicator:unchecked {image: url("+self.switch_gray_path+");} QCheckBox::indicator:checked {image: url("+self.switch_blue_path+");}")

        ## Get Python driver version 
        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    @asyncSlot() 
    async def OpenDOport(self):
       for i in range(4):
        status = await dev.DO_openPort(i)
 
        await asyncio.sleep(0.1) ## delay(second)

    @asyncSlot() 
    async def CloseDOport(self):
       for i in range(4):
        status = await dev.DO_closePort(i) 
        print("status",status)
        await asyncio.sleep(0.1) ## delay(second)

    @asyncSlot() 
    async def portEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return
 
    @asyncSlot()
    async def stateDOEvent(self):
        ## Check connection status
        if self.checkConnectionStatus() == False:
            return

        ## Initialize parameter
        self.state_cal = 0

        ## Get port from UI
        port = self.ui.combobox_port.currentIndex()

        for i in range (8):
            obj_chbox_state = getattr(self.ui, 'cb_state%d' % i) 
            state = obj_chbox_state.isChecked()
            self.state_cal += int(state) << i

        ## Set DIO to MCU
        await dev.DO_writePort(port, self.state_cal)

    @asyncSlot() 
    async def connectEvent(self):
        # Get IP from UI
        self.IP = self.ui.ld_ip.text()
        try: 
            ## Connect to network device
            dev.connect(self.IP)

            ## Change LED status
            self.ui.lb_led.setPixmap(QtGui.QPixmap(self.green_led_path))
            
            ## Change connection flag
            self.connect_flag = 1

            print(dev.DO_getPinMap())

            ## Open DO port
            self.OpenDOport()
        except pywpc.Error as err:
            # self.ui.lb_err.setText(str(err)) 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        ## Close DO port
        self.CloseDOport()

        ## Disconnect network device
        dev.disconnect() 
        
        ## Change LED status
        self.ui.lb_led.setPixmap(QtGui.QPixmap(self.gray_led_path))
        
        ## Change connection flag
        self.connect_flag = 0

    def closeEvent(self, event):
        ## Disconnect network device
        dev.disconnect()

        ## Release device handle
        dev.close()

    def checkConnectionStatus(self):
        if self.connect_flag == 0:
            QMessageBox.information(self, "Error Messages", "Please connect server first.", QMessageBox.Ok)
            return False
        else:
            return True

def main(): 
    app = QtWidgets.QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    with loop: 
        loop.run_forever()

if __name__ == "__main__":
    ## Create device handle
    dev = pywpc.USBDAQF1D()
    main()
