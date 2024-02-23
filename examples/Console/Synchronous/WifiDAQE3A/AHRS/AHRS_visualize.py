'''
AHRS - AHRS_visualize.py with synchronous mode.

This example visualize AHRS by using 3D model.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time
import numpy as np
import mpl_toolkits.mplot3d as mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.transforms import Affine2D
import matplotlib.image as mpimg
import matplotlib.font_manager as font_manager
from matplotlib import rcParams




import stl.mesh as mesh
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as mgs
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches

## WPC

from wpcsys import pywpc



################################################################################
## Configuration

DATA_PATH = 'examples/Console/Synchronous/WifiDAQE3A/AHRS/data/'
IMG_PATH = 'examples/Console/Synchronous/WifiDAQE3A/AHRS/data/avion_'



################################################################################
## Style

plt.style.use("bmh")
bmh_burgundy="#a70f34"
bmh_blue="#3d90be"
bmh_purple="#7c6ca4"


for font in font_manager.findSystemFonts(DATA_PATH):
    font_manager.fontManager.addfont(font)

# Set font family globally
rcParams['font.family'] = 'Digital-7 Mono'
    






imgname = 'WPClogo'
imgWPC = plt.imread(f'{DATA_PATH}{imgname}.jpg')

################################################################################
## Plane Images and Constants
img_yaw = mpimg.imread(f'{IMG_PATH}yaw.png')
img_pitch = mpimg.imread(f'{IMG_PATH}pitch.png')
img_roll = mpimg.imread(f'{IMG_PATH}roll.png')

size_yaw = np.array([img_yaw.shape[0], img_yaw.shape[1]])
center_yaw = size_yaw / 2
diag_yaw = np.sqrt(np.sum(size_yaw ** 2))
alpha_yaw = (diag_yaw - size_yaw) / 2
#size[1] = sixe_x and size[0] = size_y

size_pitch = np.array([img_pitch.shape[0], img_pitch.shape[1]])
center_pitch = size_pitch / 2
diag_pitch = np.sqrt(np.sum(size_pitch ** 2))
alpha_pitch = (diag_pitch - size_pitch) / 2

size_roll = np.array([img_roll.shape[0], img_roll.shape[1]])
center_roll = size_roll / 2
diag_roll = np.sqrt(np.sum(size_roll ** 2))
alpha_roll = (diag_roll - size_roll) / 2

PLANE_DICT = {
  'yaw': dict(img=img_yaw, size=size_yaw, center=center_yaw, diag=diag_yaw, alpha=alpha_yaw),
  'pitch': dict(img=img_pitch, size=size_pitch, center=center_pitch, diag=diag_pitch, alpha=alpha_pitch),
  'roll': dict(img=img_roll, size=size_roll, center=center_roll, diag=diag_roll, alpha = alpha_roll),
}

MODEL_DICT = {
  'cat': dict(label='Cat', view=400),
  'rat': dict(label='Rat', view=50),
  'rat': dict(label='Rat', view=50),
}
DEFAULT_MODEL = 'rat'

################################################################################
## Constants

DEGREE_TO_RADIAN   = np.pi / 180.0
RADIAN_TO_DEGREE   = 180.0 / np.pi


################################################################################
## Functions - utilities


def WPC_initializeFigure(nb_rows=1, nb_col=1, share_x='all', share_y='all', option='none'):
  fig = plt.figure(figsize=(10, 6))
  fig.clf()
  
  gs = gridspec.GridSpec(3, 3, width_ratios=[3, 1, 1], height_ratios=[1, 1, 1])
  ## fig = plt.gcf() ## what was initially here 
  ## fig.clf()

  ## If `option` is `3D`, return a 3-D axis.
  if option == '3D':
    ax_main = fig.add_subplot(gs[:,0], projection='3d')
    ax_main.set_title('Main 3D Plot')
    ax_plane_yaw = fig.add_subplot(gs[0, 1])
    ax_plane_pitch = fig.add_subplot(gs[1, 1])
    ax_plane_roll = fig.add_subplot(gs[2, 1])
    ax_value_yaw=fig.add_subplot(gs[0,2])
    ax_value_pitch=fig.add_subplot(gs[1,2])
    ax_value_roll=fig.add_subplot(gs[2,2])
    
    fig.figimage(imgWPC, xo=fig.bbox.xmin, yo=fig.bbox.ymin, alpha=1)

    return fig, ax_main, ax_plane_yaw, ax_plane_pitch, ax_plane_roll, ax_value_yaw, ax_value_pitch, ax_value_roll

  ## If `option` is `grid`, return gridspec for further usage.
  if option == 'grid':
    ax_grid = mgs.GridSpec(nb_rows, nb_col, figure=fig)
    return fig, None, None, ax_grid

  ## If empty rows or columns, return `None`.
  if nb_rows == 0 or nb_col == 0:
    return fig, None, None, None

  ## Return subplots
  ax_mat = fig.subplots(nb_rows, nb_col, sharex=share_x, sharey=share_y, squeeze=False)
  #sharex/sharey if the subplot would share same axis, squeeze=False to ensure ax_mat is 2D array
  ax_arr = ax_mat.flatten()
  ax = ax_arr[0]

  ## Add grid to the figure
  fig.grid(True)

  return fig, ax, ax_arr, ax_mat

def WPC_initialize_plane(angle_type,fig,ax):
  #charger l'image
  ax.set_axis_off()
  d_plane = PLANE_DICT[angle_type]
  img_plane=d_plane['img']
  im = ax.imshow(img_plane)
  
  size_plane=d_plane['size']
  center_plane=d_plane['center']
  diag_plane=d_plane['diag']
  alpha_plane=d_plane['alpha']
  tt = 1.15 #tolerance threshold of 20 percent to not have cut circle 
  
  ax.set_xlim(-alpha_plane[1]*tt, (size_plane[1] + alpha_plane[1])*tt)
  ax.set_ylim(-alpha_plane[0]*tt, (size_plane[0] + alpha_plane[0])*tt)
  ## display circle
  cc = plt.Circle((center_plane[1],center_plane[0]), diag_plane/2, fill=False, color='black', linewidth=2, linestyle = 'dashdot')
  ax.add_artist(cc) 
  return  im

def WPC_saveFigure(save, fig, tag, prefix='', verbose=True):
  if save < 0:
    tag = prefix + tag #propably a string

  save = abs(save)

  if save == 2: ## Save both PDF and PNG, transparancy on PDF
    fig.patch.set_alpha(0.5)
    name = f'{tag}.pdf'
    fig.savefig(name)

    if verbose:
      print(f'Saved \"{name}\"')

  if save in [1, 2]: ## Save PNG
    fig.patch.set_alpha(1.0)
    name = f'{tag}.png'
    fig.savefig(name)

    if verbose: 
      print(f'Saved \"{name}\"')

  if save == 0: ## Show
    w, h = fig.get_size_inches()
    fig.set_size_inches(w, h, forward=True)
    mpl.pyplot.ion() ## Turn on interactive mode
    mpl.pyplot.show()
  return

def WPC_getRotMat(roll, pitch, yaw, use_deg=False):
  if use_deg:
    roll *= DEGREE_TO_RADIAN
    pitch *= DEGREE_TO_RADIAN
    yaw *= DEGREE_TO_RADIAN
  rot_mat_x = np.array([[1, 0, 0], [0, np.cos(roll), np.sin(roll)], [0, -np.sin(roll), np.cos(roll)]])
  rot_mat_y = np.array([[np.cos(pitch), 0, np.sin(pitch)], [0, 1, 0], [-np.sin(pitch), 0, np.cos(pitch)]])
  rot_mat_z = np.array([[np.cos(yaw), -np.sin(yaw), 0], [np.sin(yaw), np.cos(yaw), 0], [0, 0, 1]])
  rot_mat = rot_mat_x.dot(rot_mat_y).dot(rot_mat_z) ## Dot product from the back RxRyRz
  return rot_mat

def WPC_showEmpty(tag=DEFAULT_MODEL, save=0):
  fig, ax_main, ax_plane_yaw, ax_plane_pitch, ax_plane_roll, ax_value_yaw, ax_value_pitch, ax_value_roll = WPC_initializeFigure(option='3D')
  im_yaw = WPC_initialize_plane('yaw',fig,ax_plane_yaw)
  im_pitch = WPC_initialize_plane('pitch',fig,ax_plane_pitch)
  im_roll = WPC_initialize_plane('roll',fig,ax_plane_roll)
  d = MODEL_DICT[tag] #model dict dictionary
  ## print("Model Dict",MODEL_DICT)

  ## Load
  model = mesh.Mesh.from_file(f'{DATA_PATH}{tag}.stl')
  data_orig = model.vectors ## 3D array

  ## Plot
  poly = mplot3d.art3d.Poly3DCollection([],color=bmh_blue, edgecolor='k', lw=0.2) #or lightsteelblue
  ax_main.add_collection3d(poly)


  ## Settings
  scale = [-0.6*d['view'], 0.6*d['view']]
  ax_main.view_init(elev=0, azim=0, roll=0)
  ax_main.auto_scale_xyz(scale, scale, scale)
  ax_main.set_axis_off()
  ax_main.set_title(f'Sensor fusion {tag}',weight='bold')
  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)
  fig.canvas.manager.set_window_title('WPC AHRS visualization')

  WPC_saveFigure(save, fig, f'{DATA_PATH}{tag}_empty')
  return fig, ax_main, data_orig, poly, ax_plane_yaw, ax_plane_pitch, ax_plane_roll, ax_value_yaw, ax_value_pitch, ax_value_roll, im_yaw, im_pitch, im_roll


def WPC_drawCat(fig, ax, data_orig, poly, roll, pitch, yaw):
  ## Rotate
  rot_mat = WPC_getRotMat(roll, pitch, yaw, use_deg=True)
  data = data_orig.dot(rot_mat)

  ## Plot
  poly.set_verts(data)
  # fig.canvas.flush_events() ## Update the 3D object

  return

#angle_type = 'yaw' for example
def WPC_plot_plane(fig,ax,angle_type,im,center):
   # Afficher l'image
  im.remove()
  # Calculer l'angle de rotation en radians
  angle = np.deg2rad(angle_type)  # Convertir en radians
  # Appliquer la rotation à l'image
  rotation_matrix = Affine2D().rotate_deg_around(center[1], center[0], np.rad2deg(angle)+180)
  im.set_transform(rotation_matrix + ax.transData)
  # Afficher à nouveau l'image
  ax.add_artist(im)
  
  return

def WPC_text_button(fig,ax,roll,pitch,yaw,ax_value_roll,ax_value_pitch,ax_value_yaw):
  for ax in [ax_value_roll,ax_value_pitch,ax_value_yaw]:
    ax.clear()
    ax.axis('off')
    ax.add_patch(plt.Rectangle((0,0), 1, 1, facecolor='#ebebeb',
                           transform=ax.transAxes, zorder=-1))
    ax.grid(False)
  Roll ="{:7.2f}".format(roll) 
  Pitch="{:7.2f}".format(pitch)
  Yaw="{:7.2f}".format(yaw)
  ax_value_roll.text(0.5, 0.5, f' Roll:\n{Roll} deg', fontsize=32,weight='bold', color=bmh_blue,ha='center',va='center')
  ax_value_pitch.text(0.5, 0.5, f' Pitch:\n{Pitch} deg', fontsize=32,weight='bold',color=bmh_burgundy,ha='center', va='center')
  ax_value_yaw.text(0.5, 0.5, f' Yaw:\n{Yaw} deg', fontsize=32,weight='bold',color=bmh_purple,ha='center', va='center')
  ax.grid(False)
  
  return
    
def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Show empty


    fig, ax, data_orig, poly, ax_plane_yaw, ax_plane_pitch, ax_plane_roll, ax_value_yaw, ax_value_pitch, ax_value_roll, im_yaw, im_pitch, im_roll = WPC_showEmpty()


    ## Connect to device
    try:
        dev.connect("192.168.5.39") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        sampling_period = 0.003 
        read_delay = 0.5 ## second
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = dev.AHRS_open(port, timeout)
        print(f"AHRS_open in port {port}: {err}")

        ## Set period
        err = dev.AHRS_setSamplingPeriod(port, sampling_period, timeout)
        print(f"AHRS_setSamplingPeriod in port {port}: {err}")

        ## Start AHRS
        err = dev.AHRS_start(port, timeout)
        print(f"AHRS_start in port {port}: {err}")

        while plt.fignum_exists(fig.number):
            ahrs_list = dev.AHRS_readStreaming(port, read_delay)
            if len(ahrs_list) > 0:
                WPC_drawCat(fig, ax, data_orig, poly, ahrs_list[0], ahrs_list[1], ahrs_list[2])
                WPC_plot_plane(fig,ax_plane_roll, ahrs_list[0], im_roll, center_roll)
                WPC_plot_plane(fig,ax_plane_pitch, ahrs_list[1], im_pitch, center_pitch)
                WPC_plot_plane(fig,ax_plane_yaw, ahrs_list[2], im_yaw, center_yaw)
                WPC_text_button(fig,ax_value_yaw, ahrs_list[0], ahrs_list[1], ahrs_list[2],ax_value_roll,ax_value_pitch,ax_value_yaw)
                plt.tight_layout()
                plt.pause(2**-5)

                #ax_low.show(img)
                #fig.canvas.flush_events()

    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop AHRS
        err = dev.AHRS_stop(port, timeout)
        print(f"AHRS_stop in port {port}: {err}")

        ## Close AHRS
        err = dev.AHRS_close(port, timeout)
        print(f"AHRS_close in port {port}: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
    return
if __name__ == '__main__':
    main()
    
## for smoother animations, search about easing ?