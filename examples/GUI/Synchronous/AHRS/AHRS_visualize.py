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
        self.dev = pywpc.WifiDAQE3AH()
        self.graphicsView = QGraphicsView()

        ## Main WWindow settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 384)
        MainWindow.setAutoFillBackground(False)
        # MainWindow.showFullScreen()

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        
        self.main_v_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_v_layout.setObjectName("main_v_layout")

        ## Input Display

        ## LineEdit, we put a default IP address
        self.input_layout = QtWidgets.QHBoxLayout()
        self.input_layout.setObjectName("input_layout")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit_ip.setMaximumWidth(300)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_ip.setText("192.168.5.39")
        self.input_layout.addWidget(self.lineEdit_ip)

        ## ComboBox, even if there is only one port, we keep it to be able to add more in the future
        self.comboBox_port = QtWidgets.QComboBox(self.central_widget)
        self.comboBox_port.addItem("0")
        self.comboBox_port.setCurrentIndex(0)
        self.comboBox_port.setObjectName("comboBox_port")
        self.input_layout.addWidget(self.comboBox_port)

        ## Start connection
        self.push_connect = QtWidgets.QPushButton(self.central_widget)
        self.push_connect.setObjectName("push_connect")
        self.input_layout.addWidget(self.push_connect)
        self.push_quitshortcut_connect = QtWidgets.QShortcut(QKeySequence(Qt.Key_Return), MainWindow)
        self.push_quitshortcut_connect.activated.connect(self.start_connection)
        self.push_connect.clicked.connect(self.start_connection)

        ## Stop connection
        self.push_stop = QtWidgets.QPushButton(self.central_widget)
        self.push_stop.setObjectName("push_stop")
        self.shortcut_stop = QtWidgets.QShortcut(QKeySequence(Qt.Key_Space), MainWindow)
        self.shortcut_stop.activated.connect(self.stop_connection)
        self.input_layout.addWidget(self.push_stop)
        self.push_stop.clicked.connect(self.stop_connection)

        ## Quit
        self.push_quit = QtWidgets.QPushButton(self.central_widget)
        self.push_quit.setObjectName("push_quit")
        self.input_layout.addWidget(self.push_quit)
        self.push_quit.clicked.connect(self.close_and_quit)
        self.shortcut_quit = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), MainWindow)
        self.shortcut_quit.activated.connect(self.close_and_quit)
        self.lineEdit_ip.setAlignment(QtCore.Qt.AlignCenter)

        ## main_v_layout
        self.main_v_layout.addLayout(self.input_layout)

        ## Prepare the layout for the all graphic parts
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")

        ## Splitter to separate the 3D graphic from the others, and give flexibility to the user:
        ## He can change the size of the 3D graphic directly on the interface
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        ## 3D graphic part
        self.mesh_widget = QtWidgets.QGraphicsView(self.central_widget)
        self.mesh_widget.setObjectName("graphicMesh")
        self.mesh_layout = QtWidgets.QGridLayout()
        self.mesh_widget.setLayout(self.mesh_layout)
        self.splitter.addWidget(self.mesh_widget)

        ## Create a widget to hold the remaining widgets
        self.graphic_widgets = QtWidgets.QWidget()
        self.right_grid_layout = QtWidgets.QGridLayout()

        ## Graphic Windows of plane images

        ## Pitch part
        self.graphic_plane_image_pitch = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_plane_image_pitch.setObjectName("graphic_plane_image_pitch")
        self.right_grid_layout.addWidget(self.graphic_plane_image_pitch, 2, 1, 1, 1)

        ## Yaw part
        self.graphic_plane_image_yaw = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_plane_image_yaw.setObjectName("graphic_plane_image_yaw")
        self.right_grid_layout.addWidget(self.graphic_plane_image_yaw, 3, 1, 1, 1)

        ## Roll part
        self.graphic_plane_image_roll = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_plane_image_roll.setObjectName("graphic_plane_image_roll")
        self.right_grid_layout.addWidget(self.graphic_plane_image_roll, 1, 1, 1, 1)

        ## Use dictionary to find it easily
        self.graphic_planes = {'yaw': self.graphic_plane_image_yaw, 'pitch': self.graphic_plane_image_pitch, 'roll': self.graphic_plane_image_roll}

        ##Graphic Windows of numeric values display of pitch, roll and yaw

        ## Pitch part
        self.graphic_text_pitch = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_text_pitch.setObjectName("graphic_text_pitch")
        self.right_grid_layout.addWidget(self.graphic_text_pitch, 2, 2, 1, 1)

        ## Yaw part
        self.graphic_text_yaw = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_text_yaw.setObjectName("graphic_text_yaw")
        self.right_grid_layout.addWidget(self.graphic_text_yaw, 3, 2, 1, 1)

        ## Roll part
        self.graphic_text_roll = QtWidgets.QGraphicsView(self.central_widget)
        self.graphic_text_roll.setObjectName("graphic_text_roll")
        self.right_grid_layout.addWidget(self.graphic_text_roll, 1, 2, 1, 1)

        self.graphic_widgets.setLayout(self.right_grid_layout)

        self.splitter.addWidget(self.graphic_widgets)
        self.grid_layout.addWidget(self.splitter, 1, 1, 3, 1)
        self.main_v_layout.addLayout(self.grid_layout)

        MainWindow.setCentralWidget(self.central_widget)

        ## Input get infos
        self.ip_address = self.lineEdit_ip.text()
        self.port = int(self.comboBox_port.currentIndex())
        self.timeout = 3 ## second
        self.sampling_period = 0.003

        self.timer_running = False ## Become True when start is pressed, to avoid multiple pressing errors
        self.quit_state = False

        ## Text Part
        self.text_scene_yaw = QGraphicsScene()
        self.text_scene_pitch = QGraphicsScene()
        self.text_scene_roll = QGraphicsScene()

        ## Create a dictionary to store the text characteristics
        self.text_items_dict = {}
        for key, props in TEXT_PROPERTIES.items():
            text_item = QtWidgets.QGraphicsTextItem(props['text'])
            text_item.setFont(props['font'])
            text_item.setDefaultTextColor(props['color'])
            self.text_items_dict[key] = text_item

        ## Add texts to graphic scenes
        for key, text_item in self.text_items_dict.items():
            scene = getattr(self, f"text_scene_{key}")
            scene.addItem(text_item)

        ## Define graphic scenes in a dictionary for an easy access
        self.graphic_text_scenes_dict = {
            'yaw': self.text_scene_yaw,
            'pitch': self.text_scene_pitch,
            'roll': self.text_scene_roll
        }

        for key, scene in self.graphic_text_scenes_dict.items():
            graphic_text_widget = getattr(self, f"graphic_text_{key}")
            graphic_text_widget.setScene(scene)

        ## Plane Part
        self.scene_plane_yaw = QGraphicsScene()
        self.scene_plane_pitch = QGraphicsScene()
        self.scene_plane_roll = QGraphicsScene()

        self.graphic_plane_image_yaw.setScene(self.scene_plane_yaw)
        self.graphic_plane_image_pitch.setScene(self.scene_plane_pitch)
        self.graphic_plane_image_roll.setScene(self.scene_plane_roll)

        self.scene_dict = {'yaw' : self.scene_plane_yaw, 'pitch' : self.scene_plane_pitch, 'roll' : self.scene_plane_roll}


        ## Load and show images in their scenes
        self.load_image(f'{IMG_PATH}yaw.png', self.scene_plane_yaw)
        self.load_image(f'{IMG_PATH}pitch.png', self.scene_plane_pitch)
        self.load_image(f'{IMG_PATH}roll.png', self.scene_plane_roll)


        self.pixmap_yaw = self.scene_plane_yaw.items()[0]
        self.width_yaw = self.pixmap_yaw.pixmap().width()
        self.height_yaw = self.pixmap_yaw.pixmap().height()
        self.center_yaw = (self.width_yaw / 2, self.height_yaw / 2)

        self.pixmap_pitch = self.scene_plane_pitch.items()[0]
        self.width_pitch = self.pixmap_pitch.pixmap().width()
        self.height_pitch = self.pixmap_pitch.pixmap().height()
        self.center_pitch = (self.width_pitch / 2, self.height_pitch / 2)

        self.pixmap_roll = self.scene_plane_roll.items()[0]
        self.width_roll = self.pixmap_roll.pixmap().width()
        self.height_roll = self.pixmap_roll.pixmap().height()
        self.center_roll = (self.width_roll / 2, self.height_roll / 2)

        ## Create dictionaries to store the pixmap and the center of the pixmap, convenient for the rotation
        self.pixmap_dict = {'yaw' : self.pixmap_yaw, 'pitch' : self.pixmap_pitch, 'roll' : self.pixmap_roll} # dictionnary to store the pixmap
        self.center_dict = {'yaw' : self.center_yaw, 'pitch' : self.center_pitch, 'roll' : self.center_roll} # dictionnary to store the center of the pixmap

        ## Initialize useful constants
        self.map_dict = {'roll' : 0, 'pitch' : 1, 'yaw' : 2}

        ## To prevent error in case of missing values, we just read the last one available
        self.list_angle = [[0,0] for i in range(3)]

        ## Mesh Part

        ## Create a widget to display 3D graphics
        self.mesh_widget = gl.GLViewWidget()

        ## Load STL mesh file
        mesh = meshio.read(f'{DATA_PATH}{TAG}.stl')

        ## Extract vertices and faces

        self.vertices = mesh.points
        self.faces = mesh.cells[0].data

        ## Create a mesh item
        self.mesh_item = gl.GLMeshItem(vertexes=self.vertices, faces=self.faces,  smooth=False, color=(152, 171, 238, 0.3))
        self.mesh_widget.addItem(self.mesh_item)
        ## Set camera position and orientation
        ## Calculate the maximum dimension of the mesh
        max_dimension = max(max(self.vertices[:, 0]) - min(self.vertices[:, 0]),
                    max(self.vertices[:, 1]) - min(self.vertices[:, 1]),
                    max(self.vertices[:, 2]) - min(self.vertices[:, 2]))

        ## Set the camera distance based on the maximum dimension
        camera_distance = max_dimension * 1.2

        self.mesh_widget.setCameraPosition(distance=camera_distance)

        ## Change displaying
        self.mesh_item.setGLOptions('additive')
        self.mesh_item.setMeshData(vertexes=self.vertices, faces=self.faces, smooth=True, color=(152, 171, 238, 0.4))

        ## Plot a grid
        grid = gl.GLGridItem()
        self.mesh_widget.addItem(grid)

        grid.scale(max_dimension, max_dimension, max_dimension)
        grid.translate(0, 0, -max_dimension * 1.2)

        ## Light blue background, set it
        self.mesh_widget.setBackgroundColor(5, 9, 27)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## Start connection
    def start_connection(self):
        if self.timer_running:
            return

        print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

        self.ip_address = self.lineEdit_ip.text()
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
        self.ahrs_list = self.dev.AHRS_getEstimate(self.port, self.mode, self.timeout)
        self.ip_address = self.lineEdit_ip.text()  # New IP address

        ## Get port from GUI
        self.port = int(self.comboBox_port.currentIndex())

        ## In case of missing values, we just read the last one available
        for type in self.map_dict.keys():
            self.list_angle[self.map_dict.get(type)] = self.list_angle[self.map_dict.get(type)][1:]
            if len(self.ahrs_list) > 0:
                angle = self.ahrs_list[self.map_dict.get(type)]
            else:
                angle = self.list_angle[self.map_dict.get(type)][-1]
            self.ahrs_list[self.map_dict.get(type)] = angle

        self.update_image_rotation_plane('yaw')
        self.update_image_rotation_plane('pitch')
        self.update_image_rotation_plane('roll')
        self.update_text()
        self.update_mesh()

    ## Simple function to align texts
    def align_texts(self, txt1, txt2, type):
        if len(txt1)>len(txt2):
            margin = (len(txt1)-len(txt2))//2
            self.text_items_dict.get(type).setPlainText(txt1+'\n'+' '*margin+txt2)
        else:
            margin = (len(txt2)-len(txt1))//2
            self.text_items_dict.get(type).setPlainText(' '*margin+txt1+'\n'+txt2)

    ## Update the text display
    def update_text(self):
        self.align_texts('Yaw', f'{self.ahrs_list[self.map_dict.get("yaw")]:.2f} deg', type='yaw')
        self.align_texts('Pitch', f'{self.ahrs_list[self.map_dict.get("pitch")]:.2f} deg', type='pitch')
        self.align_texts('Roll', f'{self.ahrs_list[self.map_dict.get("roll")]:.2f} deg', type='roll')

    ## Simple function to get the dimensions of a scene
    def get_scene_dimensions(self, scene):
        scene_x = scene.sceneRect().width()
        scene_y = scene.sceneRect().height()
        return scene_x, scene_y

    ## Update the rotation of plane images, two  opposite translations here because the rotation is done around the center of the image
    def update_image_rotation_plane(self, type):
        ## Scale the pixmap
        angle = self.ahrs_list[self.map_dict.get(type)]
        self.graphic_planes.get(type).fitInView(self.scene_dict.get(type).sceneRect(), Qt.KeepAspectRatio)

        ## Calculate center of image and create a transformation for rotation
        transform = QTransform().translate(self.center_dict.get(type)[0], self.center_dict.get(type)[1]).rotate(angle).translate(-self.center_dict.get(type)[0], -self.center_dict.get(type)[1])

        ## Apply the transformation to the pixmap
        self.pixmap_dict.get(type).setTransform(transform)

    ## Simple function to get the rotation matrix
    def WPC_getRotMat(self, use_deg=True):
        yaw, pitch, roll = self.ahrs_list[self.map_dict.get('yaw')], self.ahrs_list[self.map_dict.get('pitch')], self.ahrs_list[self.map_dict.get('roll')]
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
        self.ahrs_list = self.dev.AHRS_getEstimate(self.port, self.mode)
        ## Apply rotation to vertices
        rotated_vertices = np.dot(self.vertices, self.WPC_getRotMat().T)

        ## Update mesh with rotated vertices
        self.mesh_item.setMeshData(vertexes=rotated_vertices, faces=self.faces, smooth=True, color=(152, 171, 238, 0.4))

        ## Add the widget to the layout
        self.mesh_layout.removeWidget(self.mesh_widget)

        ## Add the widget to the layout
        self.mesh_layout.addWidget(self.mesh_widget, 0, 0, self.mesh_layout.rowCount(), 1)

    ## Function to retranslate the interface for the user
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WPC Visualisation"))
        self.push_connect.setText(_translate("MainWindow", "Start and Connect"))
        self.push_stop.setText(_translate("MainWindow", "Stop"))
        self.push_quit.setText(_translate("MainWindow", "Quit"))
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