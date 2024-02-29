##  Example_AHRS/main.py
##  This is example for demostrating AHRS with WifiDAQE3AH with synchronous mode.
##  Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
##  All rights reserved.

## For Python PYQT5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QSplashScreen, QMessageBox
from PyQt5.QtGui import QPixmap, QTransform, QKeySequence
from PyQt5.QtCore import Qt
import pyqtgraph.opengl as gl

## For Python
import time
import meshio
import numpy as np

## For WPC
from wpcsys import pywpc

## Define the data and inage path
DATA_PATH = "Material/viz_data/"
IMG_PATH = 'Material/viz_data/avion_'
TAG = 'cat'

DEGREE_TO_RADIAN = np.pi / 180.0
RADIAN_TO_DEGREE = 180.0 / np.pi

STYLE_WPC = DATA_PATH + "themeWPC.qss"
TEXT_PROPERTIES = {
            'yaw': {'text': 'C', 'font': QtGui.QFont("Arial", 38), 'color': QtGui.QColor(232, 232, 232)},
            'pitch': {'text': 'P', 'font': QtGui.QFont("Arial", 38), 'color': QtGui.QColor(232, 232, 232)},
            'roll': {'text': 'W', 'font': QtGui.QFont("Arial", 38), 'color': QtGui.QColor(232, 232, 232)} }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.dev = pywpc.WifiDAQE3A()
        self.graphicsView = QGraphicsView()

        ## Main WWindow settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 384)
        MainWindow.setAutoFillBackground(False)
        # MainWindow.showFullScreen()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.MainVlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainVlayout.setObjectName("MainVlayout")

        ## Input Display

        ## LineEdit, we put a default IP address
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        self.lineEditIP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditIP.setMaximumWidth(300)
        self.lineEditIP.setObjectName("lineEditIP")
        self.lineEditIP.setText("192.168.5.39")
        self.InputLayout.addWidget(self.lineEditIP)

        ## ComboBox, even if there is only one port, we keep it to be able to add more in the future
        self.comboBox_port = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_port.addItem("0")
        self.comboBox_port.setCurrentIndex(0)
        self.comboBox_port.setObjectName("comboBox_port")
        self.InputLayout.addWidget(self.comboBox_port)

        ## Start connection
        self.pushConnect = QtWidgets.QPushButton(self.centralwidget)
        self.pushConnect.setObjectName("pushConnect")
        self.InputLayout.addWidget(self.pushConnect)
        self.shortcutConnect = QtWidgets.QShortcut(QKeySequence(Qt.Key_Return), MainWindow)
        self.shortcutConnect.activated.connect(self.start_connection)
        self.pushConnect.clicked.connect(self.start_connection)

        ## Stop connection
        self.pushStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushStop.setObjectName("pushStop")
        self.shortcutStop = QtWidgets.QShortcut(QKeySequence(Qt.Key_Space), MainWindow)
        self.shortcutStop.activated.connect(self.stop_connection)
        self.InputLayout.addWidget(self.pushStop)
        self.pushStop.clicked.connect(self.stop_connection)

        ## Quit
        self.pushQuit = QtWidgets.QPushButton(self.centralwidget)
        self.pushQuit.setObjectName("pushQuit")
        self.InputLayout.addWidget(self.pushQuit)
        self.pushQuit.clicked.connect(self.close_and_quit)
        self.shortcutQuit = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), MainWindow)
        self.shortcutQuit.activated.connect(self.close_and_quit)
        self.lineEditIP.setAlignment(QtCore.Qt.AlignCenter)

        ## MainVlayout
        self.MainVlayout.addLayout(self.InputLayout)

        ## Prepare the layout for the all graphic parts
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        ## Splitter to separate the 3D graphic from the others, and give flexibility to the user:
        ## He can change the size of the 3D graphic directly on the interface
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        ## 3D graphic part
        self.widget3D = QtWidgets.QGraphicsView(self.centralwidget)
        self.widget3D.setObjectName("graphicMesh")
        self.meshLayout = QtWidgets.QGridLayout()
        self.widget3D.setLayout(self.meshLayout)
        self.splitter.addWidget(self.widget3D)

        ## Create a widget to hold the remaining widgets
        self.other_widgets = QtWidgets.QWidget()
        self.other_widgets_layout = QtWidgets.QGridLayout()

        ## Graphic Windows of plane images

        ## Pitch part
        self.graphicPitch = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicPitch.setObjectName("graphicPitch")
        self.other_widgets_layout.addWidget(self.graphicPitch, 2, 1, 1, 1)

        ## Yaw part
        self.graphicYaw = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicYaw.setObjectName("graphicYaw")
        self.other_widgets_layout.addWidget(self.graphicYaw, 3, 1, 1, 1)

        ## Roll part
        self.graphicRoll = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicRoll.setObjectName("graphicRoll")
        self.other_widgets_layout.addWidget(self.graphicRoll, 1, 1, 1, 1)

        ## Use dictionary to find it easily
        self.graphicPlanes = {'yaw': self.graphicYaw, 'pitch': self.graphicPitch, 'roll': self.graphicRoll}

        ##Graphic Windows of numeric values display of pitch, roll and yaw

        ## Pitch part
        self.graphicTextPitch = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicTextPitch.setObjectName("graphicTextPitch")
        self.other_widgets_layout.addWidget(self.graphicTextPitch, 2, 2, 1, 1)

        ## Yaw part
        self.graphicTextYaw = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicTextYaw.setObjectName("graphicTextYaw")
        self.other_widgets_layout.addWidget(self.graphicTextYaw, 3, 2, 1, 1)

        ## Roll part
        self.graphicTextRoll = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicTextRoll.setObjectName("graphicTextRoll")
        self.other_widgets_layout.addWidget(self.graphicTextRoll, 1, 2, 1, 1)

        self.other_widgets.setLayout(self.other_widgets_layout)

        self.splitter.addWidget(self.other_widgets)
        self.gridLayout.addWidget(self.splitter, 1, 1, 3, 1)
        self.MainVlayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        ## Input get infos
        self.ip_address = self.lineEditIP.text()
        self.port = int(self.comboBox_port.currentIndex())
        self.read_delay = 0.5 ## second
        self.timeout = 3 ## second
        self.sampling_period = 0.003

        self.timer_running = False # Become True when start is pressed, to avoid multiple pressing errors
        self.quit_state = False

        ## Text Part
        self.textSceneYaw = QGraphicsScene()
        self.textScenePitch = QGraphicsScene()
        self.textSceneRoll = QGraphicsScene()

        ## Create a dictionary to store the text characteristics
        self.textItems = {}
        for key, props in TEXT_PROPERTIES.items():
            text_item = QtWidgets.QGraphicsTextItem(props['text'])
            text_item.setFont(props['font'])
            text_item.setDefaultTextColor(props['color'])
            self.textItems[key] = text_item

        ## Add texts to graphic scenes
        for key, text_item in self.textItems.items():
            scene = getattr(self, f"textScene{key.capitalize()}")
            scene.addItem(text_item)

        ## Define graphic scenes in a dictionary for an easy access
        self.graphicTextScenes = {
            'yaw': self.textSceneYaw,
            'pitch': self.textScenePitch,
            'roll': self.textSceneRoll
        }

        for key, scene in self.graphicTextScenes.items():
            graphic_text_widget = getattr(self, f"graphicText{key.capitalize()}")
            graphic_text_widget.setScene(scene)

        ## Plane Part
        self.sceneYaw = QGraphicsScene()
        self.scenePitch = QGraphicsScene()
        self.sceneRoll = QGraphicsScene()

        self.graphicYaw.setScene(self.sceneYaw)
        self.graphicPitch.setScene(self.scenePitch)
        self.graphicRoll.setScene(self.sceneRoll)

        self.scene_dict = {'yaw' : self.sceneYaw, 'pitch' : self.scenePitch, 'roll' : self.sceneRoll}


        ## Load and show images in their scenes
        self.load_image(f'{IMG_PATH}yaw.png', self.sceneYaw)
        self.load_image(f'{IMG_PATH}pitch.png', self.scenePitch)
        self.load_image(f'{IMG_PATH}roll.png', self.sceneRoll)


        self.pixmap_Yaw = self.sceneYaw.items()[0]
        self.Yaw_width = self.pixmap_Yaw.pixmap().width()
        self.Yaw_height = self.pixmap_Yaw.pixmap().height()
        self.Yaw_center = (self.Yaw_width / 2, self.Yaw_height / 2)

        self.pixmap_Pitch = self.scenePitch.items()[0]
        self.Pitch_width = self.pixmap_Pitch.pixmap().width()
        self.Pitch_height = self.pixmap_Pitch.pixmap().height()
        self.Pitch_center = (self.Pitch_width / 2, self.Pitch_height / 2)

        self.pixmap_Roll = self.sceneRoll.items()[0]
        self.Roll_width = self.pixmap_Roll.pixmap().width()
        self.Roll_height = self.pixmap_Roll.pixmap().height()
        self.Roll_center = (self.Roll_width / 2, self.Roll_height / 2)

        ## Create dictionaries to store the pixmap and the center of the pixmap, convenient for the rotation
        self.pixmap = {'yaw' : self.pixmap_Yaw, 'pitch' : self.pixmap_Pitch, 'roll' : self.pixmap_Roll} # dictionnary to store the pixmap
        self.center = {'yaw' : self.Yaw_center, 'pitch' : self.Pitch_center, 'roll' : self.Roll_center} # dictionnary to store the center of the pixmap

        ## Initialize useful constants
        self.dict_map = {'roll' : 0, 'pitch' : 1, 'yaw' : 2}

        ## To prevent error in case of missing values, we just read the last one available
        self.list_angle = [[0,0] for i in range(3)]

        ## Mesh Part

        ## Create a widget to display 3D graphics
        self.widget3D = gl.GLViewWidget()

        ## Load STL mesh file
        mesh = meshio.read(f'{DATA_PATH}{TAG}.stl')

        ## Extract vertices and faces

        self.vertices = mesh.points
        self.faces = mesh.cells[0].data

        ## Create a mesh item
        self.mesh_item = gl.GLMeshItem(vertexes=self.vertices, faces=self.faces,  smooth=False, color=(152, 171, 238, 0.3))
        self.widget3D.addItem(self.mesh_item)
        ## Set camera position and orientation
        ## Calculate the maximum dimension of the mesh
        max_dimension = max(max(self.vertices[:, 0]) - min(self.vertices[:, 0]),
                    max(self.vertices[:, 1]) - min(self.vertices[:, 1]),
                    max(self.vertices[:, 2]) - min(self.vertices[:, 2]))

        ## Set the camera distance based on the maximum dimension
        camera_distance = max_dimension * 1.2

        self.widget3D.setCameraPosition(distance=camera_distance)

        ## Change displaying
        self.mesh_item.setGLOptions('additive')
        self.mesh_item.setMeshData(vertexes=self.vertices, faces=self.faces, smooth=True, color=(152, 171, 238, 0.4))

        ## Plot a grid
        grid = gl.GLGridItem()
        self.widget3D.addItem(grid)

        grid.scale(max_dimension, max_dimension, max_dimension)
        grid.translate(0, 0, -max_dimension * 1.2)

        ## Light blue background, set it
        self.widget3D.setBackgroundColor(5, 9, 27)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## Start connection
    def start_connection(self):
        if self.timer_running:
            return

        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        self.ip_address = self.lineEditIP.text()
        self.port = int(self.comboBox_port.currentIndex())
        try:
            self.dev.connect(self.ip_address) ## Depend on your device
        except Exception as err:
            pywpc.printGenericError(err)
            ErrorMsgBox = QMessageBox()
            ErrorMsgBox.setIcon(QMessageBox.Information)
            ErrorMsgBox.setText("Error: " + str(err))
            ErrorMsgBox.setWindowTitle("Error")
            ErrorMsgBox.setStandardButtons(QMessageBox.Ok)
            ErrorMsgBox.setStyleSheet("QLabel { color: rgba(255, 255, 255, 0.7); font-weight: bold; text-align: center; } QPushButton { border: 2px solid rgba(255, 255, 255, 0.7); border-radius: 10px; } \
                QPushButton#qt_msgbox_buttonrole { color: rgba(255, 255, 255, 0.7); }")
            ## Show the messagebox
            ErrorMsgBox.exec_()
            return

        ## Change the state of timer_running to avoid multiple pressing errors
        self.timer_running = True
        self.mode = 0
        self.dev.AHRS_open(self.port, self.timeout)
        self.dev.AHRS_setSamplingPeriod(self.port, self.sampling_period, self.timeout)
        self.dev.AHRS_start(self.port, self.timeout)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50) # 10 ms
        self.timer.timeout.connect(self.general_update)
        self.timer.start()

    ## Stop the connection, close the device and quit the application, take into account the quit_state to avoid multiple pressing errors
    def stop_connection(self):
        if not self.timer_running and not self.quit_state:
            ## Timer does not exist
            print("System not connected, can not stop.")

        elif not self.timer_running and self.quit_state:
            pass

        else:
            ## Timer does exist
            self.timer.stop()
            self.timer_running = False

            ## Stop AHRS
            self.dev.AHRS_stop(self.port, self.timeout)

            ## Close AHRS
            self.dev.AHRS_close(self.port, self.timeout)
            print(f"AHRS_close in port {self.port}")

            ## Disconnect device
            self.dev.disconnect()

    ## Close the application
    def close_and_quit(self):
        self.quit_state = True
        MainWindow.close()
        self.stop_connection()
        self.dev.close()

    ## Simple function to load an image in a scene
    def load_image(self, file_path, scene):
        pixmap = QPixmap(file_path)
        scene.addPixmap(pixmap)

    ## Update the display, calls the functions to update all sub parts of the display
    def general_update(self):
        self.ahrs_list = self.dev.AHRS_getEstimate(self.port, self.mode, self.read_delay)
        self.ip_address = self.lineEditIP.text()  # New IP address

        ## Get port from GUI
        self.port = int(self.comboBox_port.currentIndex())

        ## In case of missing values, we just read the last one available
        for type in self.dict_map.keys():
            self.list_angle[self.dict_map.get(type)] = self.list_angle[self.dict_map.get(type)][1:]
            if len(self.ahrs_list) > 0:
                angle = self.ahrs_list[self.dict_map.get(type)]
            else:
                angle = self.list_angle[self.dict_map.get(type)][-1]
            self.ahrs_list[self.dict_map.get(type)] = angle

        self.update_image_rotation_plane('yaw')
        self.update_image_rotation_plane('pitch')
        self.update_image_rotation_plane('roll')
        self.update_text()
        self.update_mesh()

    ## Simple function to align texts
    def align_texts(self, txt1, txt2, type):
        if len(txt1)>len(txt2):
            margin = (len(txt1)-len(txt2))//2
            self.textItems.get(type).setPlainText(txt1+'\n'+' '*margin+txt2)
        else:
            margin = (len(txt2)-len(txt1))//2
            self.textItems.get(type).setPlainText(' '*margin+txt1+'\n'+txt2)

    ## Update the text display
    def update_text(self):
        self.align_texts('Yaw', f'{self.ahrs_list[self.dict_map.get("yaw")]:.2f} deg', type='yaw')
        self.align_texts('Pitch', f'{self.ahrs_list[self.dict_map.get("pitch")]:.2f} deg', type='pitch')
        self.align_texts('Roll', f'{self.ahrs_list[self.dict_map.get("roll")]:.2f} deg', type='roll')

    ## Simple function to get the dimensions of a scene
    def get_scene_dimensions(self, scene):
        scene_x = scene.sceneRect().width()
        scene_y = scene.sceneRect().height()
        return scene_x, scene_y

    ## Update the rotation of plane images, two  opposite translations here because the rotation is done around the center of the image
    def update_image_rotation_plane(self, type):
        ## Scale the pixmap
        angle = self.ahrs_list[self.dict_map.get(type)]
        self.graphicPlanes.get(type).fitInView(self.scene_dict.get(type).sceneRect(), Qt.KeepAspectRatio)

        ## Calculate center of image and create a transformation for rotation
        transform = QTransform().translate(self.center.get(type)[0], self.center.get(type)[1]).rotate(angle).translate(-self.center.get(type)[0], -self.center.get(type)[1])

        ## Apply the transformation to the pixmap
        self.pixmap.get(type).setTransform(transform)

    ## Simple function to get the rotation matrix
    def WPC_getRotMat(self, use_deg=True):
        yaw, pitch, roll = self.ahrs_list[self.dict_map.get('yaw')], self.ahrs_list[self.dict_map.get('pitch')], self.ahrs_list[self.dict_map.get('roll')]
        if use_deg:
            roll *= DEGREE_TO_RADIAN
            pitch *= DEGREE_TO_RADIAN
            yaw *= DEGREE_TO_RADIAN
        rot_mat_x = np.array([[1, 0, 0], [0, np.cos(roll), np.sin(roll)], [0, -np.sin(roll), np.cos(roll)]])
        rot_mat_y = np.array([[np.cos(pitch), 0, np.sin(pitch)], [0, 1, 0], [-np.sin(pitch), 0, np.cos(pitch)]])
        rot_mat_z = np.array([[np.cos(yaw), -np.sin(yaw), 0], [np.sin(yaw), np.cos(yaw), 0], [0, 0, 1]])
        rot_mat = rot_mat_x.dot(rot_mat_y).dot(rot_mat_z) ## Dot product from the back RxRyRz
        return rot_mat

    ## Update the mesh display
    def update_mesh(self):
        self.ahrs_list = self.dev.AHRS_readStreaming(self.port, self.read_delay)
        # Apply rotation to vertices
        rotated_vertices = np.dot(self.vertices, self.WPC_getRotMat().T)

        # Update mesh with rotated vertices
        self.mesh_item.setMeshData(vertexes=rotated_vertices, faces=self.faces, smooth=True, color=(152, 171, 238, 0.4))
        # Add the widget to the layout
        self.meshLayout.removeWidget(self.widget3D)
        # Add the widget to the layout
        self.meshLayout.addWidget(self.widget3D, 0, 0, self.meshLayout.rowCount(), 1)

    ## function to retranslate the interface for the user
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WPC Visualisation"))
        self.pushConnect.setText(_translate("MainWindow", "Start and Connect"))
        self.pushStop.setText(_translate("MainWindow", "Stop"))
        self.pushQuit.setText(_translate("MainWindow", "Quit"))
        self.comboBox_port.setItemText(0, _translate("MainWindow", "Port 0"))

## Main funtion
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #display the trademark before the application starts
    splash_pix = QPixmap('Material/trademark.jpg')
    splash_pix = splash_pix.scaledToWidth(400)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()

    time.sleep(2)
    splash.finish(None)
    app.setStyleSheet(open(STYLE_WPC).read())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())