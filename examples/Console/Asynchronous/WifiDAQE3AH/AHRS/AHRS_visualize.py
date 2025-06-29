'''
AHRS - AHRS_visualize.py with asynchronous mode.

This example visualize AHRS by using 3D model.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio
import sys
sys.path.insert(0, 'src/')
import numpy as np
import stl.mesh as mesh
import mpl_toolkits.mplot3d as mplot3d
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg
import matplotlib.font_manager as font_manager
from matplotlib import rcParams
from matplotlib.transforms import Affine2D

## WPC
from wpcsys import pywpc

################################################################################
## Configuration

DATA_PATH = 'Material/viz_data/'
IMG_PATH = 'Material/viz_data/avion_'

for font in font_manager.findSystemFonts(DATA_PATH):
    font_manager.fontManager.addfont(font)

## Set font family globally
rcParams['font.family'] = 'Digital-7 Mono'

## Style
plt.style.use("bmh")
BMH_BURGUNDY = "#a70f34"
BMH_BLUE = "#3d90be"
BMH_PURPLE = "#7c6ca4"

for font in font_manager.findSystemFonts(DATA_PATH):
    font_manager.fontManager.addfont(font)

## Set font family globally
rcParams['font.family'] = 'Digital-7 Mono'

IMG_WPC = plt.imread('Material/trademark.jpg')
IMG_WPC_PIL = Image.open('Material/trademark.jpg')

################################################################################
## Plane Images and Constants

IMG_YAW = mpimg.imread(f'{IMG_PATH}yaw.png')
IMG_PITCH = mpimg.imread(f'{IMG_PATH}pitch.png')
IMG_ROLL = mpimg.imread(f'{IMG_PATH}roll.png')

SIZE_YAW = np.array([IMG_YAW.shape[0], IMG_YAW.shape[1]])
CENTER_YAW = SIZE_YAW / 2
DIAG_YAW = np.sqrt(np.sum(SIZE_YAW ** 2))
ALPHA_YAW = (DIAG_YAW - SIZE_YAW) / 2


SIZE_PITCH = np.array([IMG_PITCH.shape[0], IMG_PITCH.shape[1]])
CENTER_PITCH = SIZE_PITCH / 2
DIAG_PITCH = np.sqrt(np.sum(SIZE_PITCH ** 2))
ALPHA_PITCH = (DIAG_PITCH - SIZE_PITCH) / 2

SIZE_ROLL = np.array([IMG_ROLL.shape[0], IMG_ROLL.shape[1]])
CENTER_ROLL = SIZE_ROLL / 2
DIAG_ROLL = np.sqrt(np.sum(SIZE_ROLL ** 2))
ALPHA_ROLL = (DIAG_ROLL - SIZE_ROLL) / 2

## Dictionaries
PLANE_DICT = {
  'yaw': dict(img=IMG_YAW, size=SIZE_YAW, center=CENTER_YAW, diag=DIAG_YAW, alpha=ALPHA_YAW),
  'pitch': dict(img=IMG_PITCH, size=SIZE_PITCH, center=CENTER_PITCH, diag=DIAG_PITCH, alpha=ALPHA_PITCH),
  'roll': dict(img=IMG_ROLL, size=SIZE_ROLL, center=CENTER_ROLL, diag=DIAG_ROLL, alpha = ALPHA_ROLL),
}

MODEL_DICT = {
  'cat': dict(label='Cat', view=400),
  'rat': dict(label='Rat', view=50)
}
DEFAULT_MODEL = 'rat'

################################################################################
## Constants

DEGREE_TO_RADIAN = np.pi / 180.0
RADIAN_TO_DEGREE = 180.0 / np.pi

################################################################################
## Functions - utilities

def WPC_initializeFigure(nb_rows=1, nb_col=1, share_x='all', share_y='all', option='none'):
  fig = plt.figure(figsize=(10, 6))
  fig.clf()
  gs = gridspec.GridSpec(3, 3, width_ratios=[3, 1, 1], height_ratios=[1, 1, 1])

  ## If `option` is `3D`, return a 3-D axis.
  if option == '3D':
    ax_main = fig.add_subplot(gs[:, 0], projection='3d')
    ax_main.set_title('Main 3D Plot')
    ax_plane_yaw = fig.add_subplot(gs[0, 1])
    ax_plane_pitch = fig.add_subplot(gs[1, 1])
    ax_plane_roll = fig.add_subplot(gs[2, 1])
    ax_value_yaw = fig.add_subplot(gs[0, 2])
    ax_value_pitch = fig.add_subplot(gs[1, 2])
    ax_value_roll = fig.add_subplot(gs[2, 2])

    Pil_width = IMG_WPC_PIL.width
    Pil_height = IMG_WPC_PIL.height
    new_pil_image = IMG_WPC_PIL.resize((int(Pil_width//3), int(Pil_height//3)))
    fig.figimage(new_pil_image, xo=fig.bbox.xmin, yo=fig.bbox.ymin, alpha=0.8, zorder = 0)

    ## fig.figimage(IMG_WPC, xo=fig.bbox.xmin, yo=fig.bbox.ymin, alpha=1)
    ax_dict = {
      'main': ax_main,
      'plane_yaw': ax_plane_yaw,
      'plane_pitch': ax_plane_pitch,
      'plane_roll': ax_plane_roll,
      'value_yaw': ax_value_yaw,
      'value_pitch': ax_value_pitch,
      'value_roll': ax_value_roll,
    }

    return fig, ax_dict

  ## If `option` is `grid`, return gridspec for further usage.
  if option == 'grid':
    ax_grid = gridspec.GridSpec(nb_rows, nb_col, figure=fig)
    return fig, None, None, ax_grid

  ## If empty rows or columns, return `None`.
  if nb_rows == 0 or nb_col == 0:
    return fig, None, None, None

  ## Return subplots
  ax_mat = fig.subplots(nb_rows, nb_col, sharex=share_x, sharey=share_y, squeeze=False)

  ## sharex/sharey if the subplot would share same axis, squeeze=False to ensure ax_mat is 2D array
  ax_arr = ax_mat.flatten()
  ax = ax_arr[0]

  ## Add grid to the figure
  fig.grid(True)
  return fig, ax, ax_arr, ax_mat

def WPC_initialize_plane(angle_type, fig, ax):
  ## Load image
  ax.set_axis_off()
  d_plane = PLANE_DICT[angle_type]
  img_plane = d_plane['img']
  im = ax.imshow(img_plane)

  size_plane = d_plane['size']
  center_plane = d_plane['center']
  diag_plane = d_plane['diag']
  alpha_plane = d_plane['alpha']
  tt = 1.15 ## Tolerance threshold of 20 percent to not have cut circle

  ax.set_xlim(-alpha_plane[1]*tt, (size_plane[1] + alpha_plane[1])*tt)
  ax.set_ylim(-alpha_plane[0]*tt, (size_plane[0] + alpha_plane[0])*tt)

  ## display circle
  cc = plt.Circle((center_plane[1], center_plane[0]), diag_plane/2, fill=False, color='black', linewidth=2, linestyle='dashdot')
  ax.add_artist(cc)
  return  im

def WPC_showFigure(fig):
  w, h = fig.get_size_inches()
  fig.set_size_inches(w, h, forward=True)
  plt.ion() ## Turn on interactive mode
  plt.show()
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
  fig, ax_dict = WPC_initializeFigure(option='3D')
  im_yaw = WPC_initialize_plane('yaw', fig, ax_dict.get('plane_yaw'))
  im_pitch = WPC_initialize_plane('pitch', fig, ax_dict.get('plane_pitch'))
  im_roll = WPC_initialize_plane('roll', fig, ax_dict.get('plane_roll'))

  im_dict = {
    'yaw': im_yaw,
    'pitch': im_pitch,
    'roll': im_roll,
  }

  d = MODEL_DICT[tag] #model dict dictionary

  ## Load
  model = mesh.Mesh.from_file(f'{DATA_PATH}{tag}.stl')
  data_orig = model.vectors ## 3D array

  ## Plot
  poly = mplot3d.art3d.Poly3DCollection([], color=BMH_BLUE, edgecolor='k', lw=0.2) #or lightsteelblue
  ax_dict.get('main').add_collection3d(poly)

  ## Settings
  scale = [-0.6*d['view'], 0.6*d['view']]
  ax_dict.get('main').view_init(elev=0, azim=0, roll=0)
  ax_dict.get('main').auto_scale_xyz(scale, scale, scale)
  ax_dict.get('main').set_axis_off()
  ax_dict.get('main').set_title(f'Sensor fusion {tag}', weight='bold')

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)
  fig.canvas.manager.set_window_title('WPC AHRS visualization')

  WPC_showFigure(fig)
  return fig, ax_dict, im_dict, data_orig, poly

def WPC_draw3DModel(fig, ax, data_orig, poly, roll, pitch, yaw):
  ## Rotate
  rot_mat = WPC_getRotMat(roll, pitch, yaw, use_deg=True)
  data = data_orig.dot(rot_mat)

  ## Plot
  poly.set_verts(data)
  return

def WPC_plot_plane(fig, ax, angle_type, im, center):
  ## Display image
  im.remove()

  ## Calculate rotation angle in radians
  angle = np.deg2rad(angle_type)  #Convert in  en radians

  ## Apply rotation to the image
  rotation_matrix = Affine2D().rotate_deg_around(center[1], center[0], np.rad2deg(angle)+180)
  im.set_transform(rotation_matrix + ax.transData)

  ## Show the image again
  ax.add_artist(im)
  return

def WPC_text_button(fig, Roll, Pitch, Yaw, ax_value_roll, ax_value_pitch, ax_value_yaw):
  for ax in [ax_value_roll, ax_value_pitch, ax_value_yaw]:
    ax.clear()
    ax.axis('off')
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, facecolor='#ebebeb', transform=ax.transAxes, zorder=-1))
    ax.grid(False)
    roll = "{:7.2f}".format(Roll)
    pitch = "{:7.2f}".format(Pitch)
    yaw = "{:7.2f}".format(Yaw)
    ax_value_roll.text(0.5, 0.5, f' Roll:\n{roll} deg', fontsize=32, weight='bold', color=BMH_BLUE,ha='center', va='center')
    ax_value_pitch.text(0.5, 0.5, f' Pitch:\n{pitch} deg', fontsize=32, weight='bold', color=BMH_BURGUNDY, ha='center', va='center')
    ax_value_yaw.text(0.5, 0.5, f' Yaw:\n{yaw} deg', fontsize=32, weight='bold', color=BMH_PURPLE, ha='center', va='center')
  return

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AH()

    ## Show empty
    fig, ax_dict, im_dict, data_orig, poly = WPC_showEmpty()

    ## Connect to device
    try:
      dev.connect("192.168.5.38")  ## Depend on your device
    except Exception as err:
      pywpc.printGenericError(err)
      ## Release device handle
      dev.close()
      return

    try:
      ## Parameters setting
      port = 0  ## Depend on your device
      mode = 0 ## 0: Orientation, 1: Acceleration, 2: Orientation + Acceleration

      ## Get firmware model & version
      driver_info = await dev.Sys_getDriverInfo_async()
      print("Model name: " + driver_info[0])
      print("Firmware version: " + driver_info[-1])

      ## Open AHRS and update rate is 333 HZ
      err = await dev.AHRS_open_async(port)
      print(f"AHRS_open_async in port {port}, status: {err}")

      ## Start AHRS
      err = await dev.AHRS_start_async(port)
      print(f"AHRS_start_async in port {port}, status: {err}")

      while plt.fignum_exists(fig.number):
          ahrs_list = await dev.AHRS_getEstimate_async(port, mode)
          if len(ahrs_list) > 0:
              WPC_draw3DModel(fig, ax_dict.get('main'), data_orig, poly, ahrs_list[0], ahrs_list[1], ahrs_list[2])
              WPC_plot_plane(fig, ax_dict.get('plane_roll'), ahrs_list[0], im_dict.get('roll'), CENTER_ROLL)
              WPC_plot_plane(fig, ax_dict.get('plane_pitch'), ahrs_list[1], im_dict.get('pitch'), CENTER_PITCH)
              WPC_plot_plane(fig, ax_dict.get('plane_yaw'), ahrs_list[2], im_dict.get('yaw'), CENTER_YAW)
              WPC_text_button(fig, ahrs_list[0], ahrs_list[1], ahrs_list[2], ax_dict.get('value_roll'), ax_dict.get('value_pitch'),  ax_dict.get('value_yaw'))
              plt.tight_layout()
              plt.pause(2**-5)

    except KeyboardInterrupt:
      print("Press keyboard")

    except Exception as err:
      pywpc.printGenericError(err)

    finally:
      ## Stop AHRS
      err = await dev.AHRS_stop_async(port)
      print(f"AHRS_stop_async in port {port}, status: {err}")

      ## Close AHRS
      err = await dev.AHRS_close_async(port)
      print(f"AHRS_close_async in port {port}, status: {err}")

      ## Disconnect device
      dev.disconnect()

      ## Release device handle
      dev.close()
    return
def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
