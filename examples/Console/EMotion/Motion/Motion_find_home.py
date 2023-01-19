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
        rel_posi_mode = 1
        stop_decel = 0 
        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0
        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1
        home_enable_false = 0
        ## Find home parameters
        find_home = 0 
        search_dir_rev = 1
 
        ## Motion open
        err = await dev.Motion_open_async(port)
        print("open_async:", err)

        ## Motion configure
        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print("cfgAxis_async:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis, forward_enable_true, reverse_enable_true, active_high)
        print("cfgLimit_async:", err)

        err = await dev.Motion_cfgFindRef_async(port, axis, find_home, search_dir_rev)
        print("cfgFindRef_async:", err)

        err = await dev.Motion_cfgHome_async(port, axis, home_enable_false, active_high)
        print("cfgHome_async:", err)
        
        err = await dev.Motion_enableServoOn_async(port, axis, int(True))
        print("enableServoOn_async:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis)
        print("rstEncoderPosi_async:", err)

        ## Motion find reference
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
         
        ## Motion stop
        err = await dev.Motion_stop_async(port, axis, stop_decel)
        print("stop_async:", err) 
 
        err = await dev.Motion_enableServoOn_async(port, axis, int(False))
        print("enableServoOn_async:", err)

        ## Motion close
        err = await dev.Motion_close_async(port)
        print("close_async:", err)  
         
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