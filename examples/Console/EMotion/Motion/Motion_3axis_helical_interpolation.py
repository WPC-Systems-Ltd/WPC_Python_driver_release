'''
Motion - Motion_3axis_helical_interpolation.py
 
For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
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
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        axis1 = 0
        center_x = 0
        center_y = 0
        finish_x = 100
        finish_y = 100
        pitch_axis3 = 0
        pitch_axis4 = 0
        rotation_num = 0
        speed = 0 
        cal_timeout = 1000
        dir_cw = 0
        stop_deceleration = 0

        err = await dev.Motion_open_async(port)
        print("open_async:", err)
        
        err = await dev.Motion_opencfgFile_async('3AxisStage_2P.ini')
        print("opencfgFile_async:", err)

        err = await dev.Motion_loadCfgFile_async()
        print("loadCfgFile_async:", err)

        err = await dev.Motion_cfgHelicalInterpo_async(port, center_x, center_y, finish_x, finish_y, int(False), pitch_axis3, int(False), pitch_axis4, rotation_num,
        speed, dir_cw, cal_timeout)
        print("cfgHelicalInterpo_async:", err) 
 
        err = await dev.Motion_startHelicalInterpo_async(port)
        print("startHelicalInterpo_async:", err)
  
        move_status = 0; 
        while move_status == 0:
            move_status = await dev.Motion_getMoveStatus_async(port, axis1) 
            print("getMoveStatus_async:", move_status) 
  
        err = await dev.Motion_stop_async(port, axis1, stop_deceleration)
        print("stop_async:", err) 
 
        err = await dev.Motion_close_async(port)
        print("close_async:", err) 
         
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return

if __name__ == '__main__':
    asyncio.run(main())