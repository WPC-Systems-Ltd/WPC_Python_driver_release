'''
Motion - Motion_1axis_move_with_configuration_file.py with asynchronous mode.
 
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
        rel_posi_mode = 1
        stop_decel = 0

        ## Motion open
        err = await dev.Motion_open_async(port)
        print("open_async:", err)
 
        ## Motion open configuration file
        err = await dev.Motion_opencfgFile_async('3AxisStage_2P.ini')
        print("opencfgFile_async:", err)

        ## Motion load configuration file
        err = await dev.Motion_loadCfgFile_async()
        print("loadCfgFile_async:", err)

        ## Motion configure
        err = await dev.Motion_cfgAxisMove_async(port, axis, rel_posi_mode, target_position = 5000)
        print("cfgAxisMove_async:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis)
        print("rstEncoderPosi_async:", err)

        err = await dev.Motion_enableServoOn_async(port, axis, int(True))
        print("enableServoOn_async:", err)

        ## Motion start
        err = await dev.Motion_startSingleAxisMove_async(port, axis)
        print("startSingleAxisMove_async:", err)

        move_status = 0; 
        while move_status == 0:
            move_status = await dev.Motion_getMoveStatus_async(port, axis)
            print("getMoveStatus_async:", move_status)
            
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