'''
Motion - Motion_2axis_linear_interpolation.py
 
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
        dest_posi1 = 2000
        axis2 = 1
        dest_posi2 = 2000 
        stop_deceleration = 0

        err = await dev.Motion_open_async(port)
        print("open_async:", err)
        
        err = await dev.Motion_opencfgFile_async('3AxisStage_2P.ini')
        print("opencfgFile_async:", err)

        err = await dev.Motion_loadCfgFile_async()
        print("loadCfgFile_async:", err)

        err = await dev.Motion_cfg2AxisLinearInterpo_async(port, axis1, dest_posi1, axis2, dest_posi2, speed = 2000)
        print("cfg2AxisLinearInterpo_async:", err) 

        err = await dev.Motion_startLinearInterpo_async(port)
        print("startLinearInterpo_async:", err)
  
        move_status = 0; 
        while move_status == 0:
            axis1_move_status = await dev.Motion_getMoveStatus_async(port, axis1)
            axis2_move_status = await dev.Motion_getMoveStatus_async(port, axis2)
            move_status = axis1_move_status & axis2_move_status;  
            if move_status == 0: 
                print("Moving......") 
            else:
                print("Move completed") 
 
        err = await dev.Motion_stop_async(port, axis1, stop_deceleration)
        print("stop_async axis1 :", err) 
        
        err = await dev.Motion_stop_async(port, axis2, stop_deceleration)
        print("stop_async axis2 :", err)
        
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