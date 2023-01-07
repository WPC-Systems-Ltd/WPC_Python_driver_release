'''
Motion - Motion_find_home.py
 
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
        axis = 0
        two_pulse_mode = 1
        relative_position = 1
        dir_cw = 0
        active_low = 0
        active_high = 1
        stop_deceleration = 0 
        find_home = 0
        dir_reverse = 1

        err = await dev.Motion_open_async(port)
        print("open_async:", err)

        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, dir_cw, dir_cw, active_low)
        print("cfgAxis_async:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis, int(True), int(True), active_high)
        print("cfgLimit_async:", err)

        err = await dev.Motion_cfgFindRef_async(port, axis, find_home, dir_reverse)
        print("cfgFindRef_async:", err)

        err = await dev.Motion_cfgHome_async(port, axis, int(False), active_high)
        print("cfgHome_async:", err)
        
        err = await dev.Motion_enableServoOn_async(port, axis, int(True))
        print("enableServoOn_async:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis)
        print("rstEncoderPosi_async:", err)

        err = await dev.Motion_findRef_async(port, axis)
        print("findRef_async:", err)
        
        home_status = 0 
        while home_status == 0: 
            ## Read forward and reverse limit status
            hit_status = await dev.Motion_getLimitStatus_async(port, axis)
            forward_hit = hit_status[0]
            reverse_hit = hit_status[1]
            if forward_hit == 1 : print("Forward hit")
            if reverse_hit == 1 : print("Reverse hit")

            ## Read home status
            home_status = await dev.Motion_getHomeStatus_async(port, axis)
            if home_status == 1 : print("Home hit")
            
            ## Check finding and found status
            driving_status = await dev.Motion_checkRef_async(port, axis)
            finding = driving_status[0]
            found = driving_status[1]
            if found == 1 : print("Found reference")
            # if finding == 1 : print("Finding reference")
         
        err = await dev.Motion_stop_async(port, axis, stop_deceleration)
        print("stop_async:", err) 

        err = await dev.Motion_enableServoOn_async(port, axis, int(False))
        print("enableServoOn_async:", err)
        
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