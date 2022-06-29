from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from Ui_example_GUI_AIStreaming import Ui_MainWindow 
from qasync import QEventLoop, asyncSlot
import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc  
import matplotlib.animation as animation
import numpy as np

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent) 

 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ## UI initialize
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # - Connection flag
        self.connect_flag = 0

        # - plot parameter
        self.plot_y_min = -10
        self.plot_y_max = 10

        # - ai parameter
        self.ai_sampling_rate = 1000
        self.ai_n_samples = 200
 
        # - list parameter
        self.channel_list = []
        for j in range(8):
            self.channel_list.append([])
        self.plot_total_times = 0

        ## Define button callback events
        self.ui.btn_connect.clicked.connect(self.connectEvent)
        self.ui.btn_disconnect.clicked.connect(self.disconnectEvent) 
        self.ui.btn_AIStart.clicked.connect(self.startAIEvent)
        self.ui.btn_AIStop.clicked.connect(self.stopAIEvent)

        # - Line edit
        self.ui.lineEdit_samplingRate.returnPressed.connect(self.setSamplingRateEvent)
        self.ui.lineEdit_numSamples.returnPressed.connect(self.setNumofSampleEvent)
        
        # - ComboBox
        self.ui.comboBox_aiMode.currentIndexChanged.connect(self.chooseAIModeEvent) 
        self.ui.lineEdit_yscaleMax.returnPressed.connect(self.setYscaleMaxEvent)
        self.ui.lineEdit_yscaleMin.returnPressed.connect(self.setYscaleMinEvent)


        # - Get WPC Driver version
        str_ = f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}'
        print(str_)

        # - Plotting
        self.plotInitial()
        self.plotAnimation()

        # - Function loop
        self.loop_fct(0.05)   ## 0.05s = 50 ms

    def plotInitial(self):
        self.checkboxstatus = [1 for x in range(8)]
        self.matplotlibwidget = MatplotlibWidget()
   
        for i in range(8):
            self.ui.MplWidget.canvas.axes.plot([0], [0], alpha=self.checkboxstatus[i])

              
    # Define matplotlib animation input function
    def plotAnimation(self):
        self.ani = animation.FuncAnimation(self.ui.MplWidget, self.plotChart, self.plotGetAxisData, interval=100, repeat=True)
        self.ui.MplWidget.canvas.draw()
        # Rearrage x-axis data according to data amount
    
    def plotGetAxisData(self):
        # Get ch0~ch7 checkbox status from MainUI window
        list_ch = [self.ui.cb_ch0, self.ui.cb_ch1, self.ui.cb_ch2, self.ui.cb_ch3, self.ui.cb_ch4, self.ui.cb_ch5,self.ui.cb_ch6, self.ui.cb_ch7]
        for i in range(8):
            self.checkboxstatus[i] = int(list_ch[i].isChecked())

        # Get xmin, xmax and x list
        m = len(self.channel_list[0])
        x_max = self.plot_total_times
        x_min = max(x_max - m, 0)
        x_list = list(range(x_min, x_max))

        # Get xticks
        if m > 5:
            dx = m // 6
            ticks = np.arange(x_min, x_max, dx)
        else:
            ticks = np.arange(x_min, x_max)

        yield x_list, ticks, x_min, x_max, self.checkboxstatus

    # Plotting AI streaming
    def plotChart(self, update):
        # Define update value
        x_list, ticks, x_min, x_max, self.checkboxstatus = update
 
        # Clear all axes info
        self.ui.MplWidget.canvas.axes.clear()
        
        # Plot 8 channels data

        try:
            for i in range(8):
                self.ui.MplWidget.canvas.axes.plot(x_list, self.channel_list[i], alpha=self.checkboxstatus[i],
                                                marker='o', markersize=2)
        except:
            print("err_xlist " + str(len(x_list)))
            print("err_ylist " + str(len(self.channel_list[i])))


        # Set x,y limit
        self.ui.MplWidget.canvas.axes.set_ylim(float(self.plot_y_min) * 1.05, float(self.plot_y_max) * 1.05)
        self.ui.MplWidget.canvas.axes.set_xlim(x_min, x_max)

        # Set xtickslabel
        self.ui.MplWidget.canvas.axes.set_xticks(ticks)
        new_ticks = self.plotConvtXtick(ticks)
        self.ui.MplWidget.canvas.axes.set_xticklabels(new_ticks)

        # Set label
        self.ui.MplWidget.canvas.axes.set_xlabel("Time (s)", fontsize=12)
        self.ui.MplWidget.canvas.axes.set_ylabel("Voltage (V)", fontsize=12)

        # Set legend
        self.ui.MplWidget.canvas.axes.legend(('ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'),
                                            loc='center left', shadow=False, fontsize=10, bbox_to_anchor=(1, 0.75),
                                            facecolor='#f0f0f0')
        # Set grid
        self.ui.MplWidget.canvas.axes.grid(color='#bac3d1', linestyle='-', linewidth=0.8)  # grid

    def plotConvtXtick(self, xtick):
        return ["{:.2f}".format(x / self.ai_sampling_rate) for i, x in enumerate(xtick)]

 
    def setDisplayPlotNums(self, data, nums):
        data = np.array(data)
        self.plot_total_times += len(data)
        
        # for plotting
        for k in range(8):
            self.channel_list[k].extend(data[:, k])
            self.channel_list[k] = self.channel_list[k][-(nums):]
    @asyncSlot() 
    async def loop_fct(self, delay): 
        while True: 
            data = await dev.readAIStreaming(500, delay)
            if data is not None:
                self.setDisplayPlotNums(data, self.ai_n_samples)
            else: 
                await asyncio.sleep(delay) 

    @asyncSlot()      
    async def startAIEvent(self):
        get_mode = self.ui.comboBox_aiMode.currentIndex()
        if get_mode == 0: ## On Demand
            ondemanddata = await dev.readAIOnDemand()
            self.setDisplayPlotNums([ondemanddata], self.ai_n_samples)
        else: ## N-Samples/ Continuous 
            await dev.startAI()

    @asyncSlot()      
    async def stopAIEvent(self):
        await dev.stopAI()


    @asyncSlot()
    # AI mode for MCU parameter
    async def chooseAIModeEvent(self, *args):
        # Check connection status
        if self.checkConnectionStatus() == False:
            return
        # Get AI mode from MainUI window
        get_mode = int(self.ui.comboBox_aiMode.currentIndex())
        # Send command to MCU
        await dev.setAIMode(get_mode) ## 2 is continuous mode 

    @asyncSlot()
    # Sampling rate for MCU parameter
    async def setSamplingRateEvent(self):
        # Check connection status
        if self.checkConnectionStatus() == False:
            return
        # Get Sampling rate from MainUI window
        sampling_rate = float(self.ui.lineEdit_samplingRate.text())
        ai_sampling_rate = sampling_rate
        # Send command to MCU
        await dev.setAISamplingRate(sampling_rate)


    @asyncSlot()
    # NumofSample for MCU parameter
    async def setNumofSampleEvent(self):
        # Check connection status
        if self.checkConnectionStatus() == False:
            return
        # Get NumSamples from MainUI window
        n_samples = int(self.ui.lineEdit_numSamples.text())
        self.ai_n_samples = n_samples
        # Send command to MCU
        await dev.setAINumSamples(n_samples)
 
    
    # y_max for plotting parameter
    def setYscaleMaxEvent(self):
        # Check connection status
        if self.checkConnectionStatus() == False:
            return
        # Get yscaleMax from MainUI window
        self.plot_y_max = self.ui.lineEdit_yscaleMax.text()

    # y_min for plotting parameter
    def setYscaleMinEvent(self):
        # Check connection status
        if self.checkConnectionStatus() == False:
            return
        # Get yscaleMin from MainUI window
        self.plot_y_min = self.ui.lineEdit_yscaleMin.text()

    # Check TCP connection with QMessageBox
    def checkConnectionStatus(self):
        if self.connect_flag == 1:
            QMessageBox.information(self, "Error Messages", "Please connect server first.", QMessageBox.Ok)
            return False
        else:
            return True
 
    @asyncSlot()      
    async def connectEvent(self): 
        # Get ip from MainUI window
        self.ip = self.ui.lineEdit_ip.text()
        try: 
            dev.connect(self.ip) 
        except pywpc.Error as err: 
            print("err: " + str(err))

    @asyncSlot()      
    async def disconnectEvent(self): 
        dev.disconnect() 

    def closeEvent(self, event):  
        dev.disconnect() ## Don't forget to close connection
        dev.close()  ## Don't forget to free in order to kill the threads
         
  
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
