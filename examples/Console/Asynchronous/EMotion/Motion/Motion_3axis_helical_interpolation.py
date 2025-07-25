'''
Motion - Motion_3axis_helical_interpolation.py with asynchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc

## Python
import asyncio
import sys
sys.path.insert(0, 'src/')


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        axis = 0
        stop_decel = 0

        ## Helical parameters
        center_x = 0
        center_y = 0
        finish_x = 100
        finish_y = 100
        pitch_axis3 = 0
        pitch_axis4 = 0
        rotation_num = 0
        speed = 0
        cal_timeout = 1000
        helical_dir_cw = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"open_async in port {port}, status: {err}")

        ## Motion open configuration file
        err = await dev.Motion_openCfgFile_async('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"openCfgFile_async, status: {err}")

        ## Motion load configuration file
        err = await dev.Motion_loadCfgFile_async()
        print(f"loadCfgFile_async, status: {err}")

        ## Motion configure
        err = await dev.Motion_cfgHelicalInterpo_async(port, center_x, center_y, finish_x, finish_y, int(False), pitch_axis3, int(False), pitch_axis4, rotation_num,
                                                       speed, helical_dir_cw, cal_timeout)
        print(f"cfgHelicalInterpo_async in axis{axis}, status: {err}")

        ## Motion start
        err = await dev.Motion_startHelicalInterpo_async(port)
        print(f"startHelicalInterpo_async in axis{axis}, status: {err}")

        move_status = 0
        while move_status == 0:
            move_status = await dev.Motion_getMoveStatus_async(port, axis)
            print(f"getMoveStatus_async in axis{axis}: {move_status}")

        ## Motion stop
        err = await dev.Motion_stop_async(port, axis, stop_decel)
        print(f"stop_async in axis{axis}, status: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"close_async in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
