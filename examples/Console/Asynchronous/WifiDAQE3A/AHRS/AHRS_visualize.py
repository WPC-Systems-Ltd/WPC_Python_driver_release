'''
AHRS - AHRS_visualize.py with asynchronous mode.

This example visualize AHRS by using 3D model.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio
import numpy as np
import mpl_toolkits.mplot3d as mplot3d
import stl.mesh as mesh
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as mgs

## WPC

from wpcsys import pywpc


################################################################################
## Configuration
DATA_PATH = 'examples/Console/Asynchronous/WifiDAQE3A/AHRS/data/'
IMG_PATH = 'images/'
MODEL_DICT = {
  'cat': dict(label='Cat', view=400),
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
  fig = plt.gcf()
  fig.clf()

  ## If `option` is `3D`, return a 3-D axis.
  if option == '3D':
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    return fig, ax, None, None

  ## If `option` is `grid`, return gridspec for further usage.
  if option == 'grid':
    ax_grid = mgs.GridSpec(nb_rows, nb_col, figure=fig)
    return fig, None, None, ax_grid

  ## If empty rows or columns, return `None`.
  if nb_rows == 0 or nb_col == 0:
    return fig, None, None, None

  ## Return subplots
  ax_mat = fig.subplots(nb_rows, nb_col, sharex=share_x, sharey=share_y, squeeze=False)
  ax_arr = ax_mat.flatten()
  ax = ax_arr[0]
  return fig, ax, ax_arr, ax_mat

def WPC_saveFigure(save, fig, tag, prefix='', verbose=True):
  if save < 0:
    tag = prefix + tag

  save = abs(save)

  if save == 2:
    fig.patch.set_alpha(0.5)
    name = f'{tag}.pdf'
    fig.savefig(name)

    if verbose:
      print(f'Saved \"{name}\"')

  if save in [1, 2]:
    fig.patch.set_alpha(1.0)
    name = f'{tag}.png'
    fig.savefig(name)

    if verbose:
      print(f'Saved \"{name}\"')

  if save == 0:
    w, h = fig.get_size_inches()
    fig.set_size_inches(w, h, forward=True)
    mpl.pyplot.ion()
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
  rot_mat = rot_mat_x.dot(rot_mat_y).dot(rot_mat_z) ## Dot product from the back
  return rot_mat

def WPC_showEmpty(tag=DEFAULT_MODEL, save=0):
  fig, ax, _, _ = WPC_initializeFigure(option='3D')

  d = MODEL_DICT[tag]

  ## Load
  model = mesh.Mesh.from_file(f'{DATA_PATH}{tag}.stl')
  data_orig = model.vectors

  ## Plot
  poly = mplot3d.art3d.Poly3DCollection([], color='orange', edgecolor='k', lw=0.2)
  ax.add_collection3d(poly)

  ## Settings
  scale = [-0.6*d['view'], 0.6*d['view']]
  ax.view_init(elev=0, azim=0, roll=0)
  ax.auto_scale_xyz(scale, scale, scale)
  ax.set_axis_off()
  ax.set_title(f'sensor fusion {tag}')
  ax.text2D(0.7, 0.95, "Roll:", transform=ax.transAxes)
  ax.text2D(0.7, 0.9, "Pitch:", transform=ax.transAxes)
  ax.text2D(0.7, 0.85, "Yaw:", transform=ax.transAxes)

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)
  fig.canvas.manager.set_window_title('WPC AHRS visualization')

  WPC_saveFigure(save, fig, f'{IMG_PATH}{tag}_empty')
  return fig, ax, data_orig, poly

def WPC_drawCat(fig, ax, data_orig, poly, roll, pitch, yaw):
  ## Rotate
  rot_mat = WPC_getRotMat(roll, pitch, yaw, use_deg=True)
  data = data_orig.dot(rot_mat)

  Roll = "{:7.2f}".format(roll)
  Pitch = "{:7.2f}".format(pitch)
  Yaw = "{:7.2f}".format(yaw)

  tx1 = ax.text2D(0.78, 0.95, Roll, transform=ax.transAxes)
  tx2 = ax.text2D(0.78, 0.9, Pitch, transform=ax.transAxes)
  tx3 = ax.text2D(0.78, 0.85, Yaw, transform=ax.transAxes)

  ## Plot
  poly.set_verts(data)
  fig.canvas.flush_events()

  tx1.remove()
  tx2.remove()
  tx3.remove()
  return

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Show empty
    fig, ax, data_orig, poly = WPC_showEmpty()

    ## Connect to device
    try:
        dev.connect("192.168.5.38") ## Depend on your device
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

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = await dev.AHRS_open_async(port)
        print(f"AHRS_open_async in port {port}: {err}")

        ## Set period
        err = await dev.AHRS_setSamplingPeriod_async(port, sampling_period)
        print(f"AHRS_setSamplingPeriod_async in port {port}: {err}")

        ## Start AHRS
        err = await dev.AHRS_start_async(port)
        print(f"AHRS_start_async in port {port}: {err}")

        while True:
            ahrs_list = await dev.AHRS_readStreaming_async(port, read_delay)
            if len(ahrs_list) > 0:
                WPC_drawCat(fig, ax, data_orig, poly, ahrs_list[0], ahrs_list[1], ahrs_list[2])

    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop AHRS
        err = await dev.AHRS_stop_async(port)
        print(f"AHRS_stop_async in port {port}: {err}")

        ## Close AHRS
        err = await dev.AHRS_close_async(port)
        print(f"AHRS_close_async in port {port}: {err}")

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
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder