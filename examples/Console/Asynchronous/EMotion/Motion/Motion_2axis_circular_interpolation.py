'''
Motion - Motion_2axis_circular_interpolation.py with asynchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        axis = 0
        stop_decel = 0
        rel_posi_mode = 1

        ## Circular interpolation parameters
        x_axis = 0
        y_axis = 1
        center_point_x = 2000
        center_point_y = 2000
        finish_point_x = 0
        finish_point_y = 0
        circular_dir_cw = 0

        ## jerk and acceletation mode parameters setting
        scurve = 1
        jerk = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"open_async in port {port}: {err}")

        ## Motion open configuration file
        err = await dev.Motion_openCfgFile_async('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"openCfgFile_async: {err}")

        ## Motion load configuration file
        err = await dev.Motion_loadCfgFile_async()
        print(f"loadCfgFile_async: {err}")

        ## Motion configure
        err = await dev.Motion_cfgCircularInterpo_async(port, x_axis, y_axis, center_point_x, center_point_y, finish_point_x, finish_point_y, circular_dir_cw, speed=1000, accel=100000, decel=100000)
        print(f"cfgCircularInterpo_async in port {port}: {err}")

        err = await dev.Motion_startCircularInterpo_async(port)
        print(f"startCircularInterpo_async in axis{axis}: {err}")

        err = await dev.Motion_cfgAxisMove_async(port, axis, rel_posi_mode, target_posi=5000, velo=10000, accel=100000, decel=100000)
        print(f"cfgAxisMove_async in axis{axis}: {err}")

        err = await dev.Motion_cfgJerkAndAccelMode_async(port, axis, jerk, scurve)
        print(f"cfgJerkAndAccelMode_async in axis{axis}: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis, encoder_posi=0)
        print(f"rstEncoderPosi_async in axis{axis}: {err}")

        for i in range(4):
            err = await dev.Motion_enableServoOn_async(port, i)
            print(f"enableServoOn_async in axis{i}: {err}")

        ## Motion start
        err = await dev.Motion_startSingleAxisMove_async(port, axis)
        print(f"startSingleAxisMove_async in axis{axis}: {err}")

        move_status = 0
        while move_status == 0:
            x_axis_move_status = await dev.Motion_getMoveStatus_async(port, x_axis)
            y_axis_move_status = await dev.Motion_getMoveStatus_async(port, y_axis)
            move_status = x_axis_move_status & y_axis_move_status
            if move_status == 0:
                print("Moving......")
            else:
                print("Move completed")

        ## Motion stop
        err = await dev.Motion_stop_async(port, axis, stop_decel)
        print(f"stop_async in axis{axis}: {err}")

        for i in range(4):
            err = await dev.Motion_enableServoOff_async(port, i)
            print(f"enableServoOff_async in axis{i}: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"close_async in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

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