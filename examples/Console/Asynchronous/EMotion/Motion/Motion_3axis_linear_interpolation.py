'''
Motion - Motion_3axis_linear_interpolation.py with asynchronous mode.

--------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
        stop_decel = 0

        ## Linear interpolation parameters
        axis1 = 0
        dest_posi1 = 2000
        axis2 = 1
        dest_posi2 = 2000
        axis3 = 2
        dest_posi3 = 2000

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
        err = await dev.Motion_cfg3AxisLinearInterpo_async(port, axis1, dest_posi1, axis2, dest_posi2, axis3, dest_posi3, speed=2000, accel=100000, decel=100000)
        print(f"cfg3AxisLinearInterpo_async in port {port}: {err}")

        ## Motion start
        err = await dev.Motion_startLinearInterpo_async(port)
        print(f"startLinearInterpo_async in port {port}: {err}")

        move_status = 0
        while move_status == 0:
            axis1_move_status = await dev.Motion_getMoveStatus_async(port, axis1)
            axis2_move_status = await dev.Motion_getMoveStatus_async(port, axis2)
            axis3_move_status = await dev.Motion_getMoveStatus_async(port, axis3)
            move_status = axis1_move_status & axis2_move_status & axis3_move_status
            if move_status == 0:
                print("Moving......")
            else:
                print("Move completed")

        ## Motion stop
        for i in [axis1, axis2, axis3]:
            err = await dev.Motion_stop_async(port, i, stop_decel)
            print(f"stop_async axis{i}  in port {port}: {err}")

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