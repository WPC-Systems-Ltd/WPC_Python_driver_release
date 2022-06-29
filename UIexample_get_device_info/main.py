from PyQt5 import QtWidgets
from Ui_example_GUI_Get_Device_Information import Ui_MainWindow 
from qasync import QEventLoop, asyncSlot
import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        ## initialize param
        self.connect_flag = 0
        
        ## Define button callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent)
        self.ui.btn_deviceInfo.clicked.connect(self.getdeviceinfoEvent)

        ## Get WPC Driver version
        str_ = f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}'
        print(str_)
    
 
    @asyncSlot()      
    async def connectEvent(self):
        self.clearErrorStatus()
        # Get ip from MainUI window
        self.ip = self.ui.lineEdit_ipConnect.text()
        try: 
            dev.connect(self.ip)
        except pywpc.Error as err:
            self.ui.lb_err.setText(str(err)) 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self):
        dev.disconnect()


    @asyncSlot()      
    async def getdeviceinfoEvent(self):
        self.clearErrorStatus()
        print('test')
        firmware_info = await dev.getDriverInfo()
        print(firmware_info) 
        str_list = firmware_info.split('_')
        model = str_list[0]
        version = str_list[1] 
        ip, submask = await dev.getIPAddrAndSubmask()
        serial_number = await dev.getSerialNumber()
        mac = await dev.getMACAddr()
        rtc = await dev.getRTCDateTime()

        self.ui.lineEdit_ip.setText(ip)
        self.ui.lineEdit_sbk.setText(submask)
        self.ui.lineEdit_serialNum.setText(serial_number)
        self.ui.lineEdit_mac.setText(mac)
        self.ui.lineEdit_model.setText(model)
        self.ui.lineEdit_version.setText(version)
        self.ui.lineEdit_rtc.setText(rtc)
  
    def closeEvent(self, event):
        dev.disconnect()
        dev.close()
         
    def clearErrorStatus(self):
        self.ui.lb_err.clear()

def main(): 
    app = QtWidgets.QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop) 
    WPC_main_ui = MainWindow()
    WPC_main_ui.show() 
    with loop: 
        loop.run_forever()

if __name__ == "__main__":
    ## Create handle 
    dev = pywpc.WifiDAQ()
    main()
