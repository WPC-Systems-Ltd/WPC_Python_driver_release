# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure


class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)


        self.canvas = FigureCanvas(Figure(figsize = (18, 6), dpi = 100))

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
 
        self.canvas.figure.patch.set_facecolor("#f0f0f0")
        self.canvas.axes.set_facecolor("#f0f0f0")  # Change axis color
        self.canvas.axes.tick_params('both', direction='in')
        self.canvas.axes.patch.set_alpha(0.5)
        self.canvas.axes.tick_params(labelsize=10)
        self.canvas.axes.set_ylim(-10 * 1.05, 10 * 1.05)
        self.canvas.axes.grid(color='#bac3d1', linestyle='-', linewidth=0.8)  # grid
        self.canvas.axes.set_xlabel("Time (s)", fontsize=12)
        self.canvas.axes.set_ylabel("Voltage (V)", fontsize=12)
   
        self.canvas.axes.legend(('ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'),
                                             loc='center left', shadow=False, fontsize=10, bbox_to_anchor=(1, 0.75),
                                             facecolor='#f0f0f0')

        self.setLayout(vertical_layout)