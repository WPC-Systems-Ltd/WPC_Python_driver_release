'''
Motion - Motion_find_limit.py with asynchronous mode.

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
        two_pulse_mode = 1
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

        ## Find limit parameters
        find_limit = 2
        dir_reverse = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"open_async in port {port}: {err}")

        '''
        ## Motion open configuration file
        err = await dev.Motion_openCfgFile_async('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"openCfgFile_async: {err}")

        ## Motion load configuration file
        err = await dev.Motion_loadCfgFile_async()
        print(f"loadCfgFile_async: {err}")
        '''

        ## Motion configure
        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print(f"cfgAxis_async in axis{axis}: {err}")

        err = await dev.Motion_cfgLimit_async(port, axis, forward_enable_true, reverse_enable_true, active_low)
        print(f"cfgLimit_async in axis{axis}: {err}")

        err = await dev.Motion_cfgFindRef_async(port, axis, find_limit, dir_reverse, search_velo=10000, search_accle=100000, approach_velo_percent=20, en_reset_posi=0, offset_posi=1500)
        print(f"cfgFindRef_async in axis{axis}: {err}")

        err = await dev.Motion_cfgHome_async(port, axis, home_enable_false, active_low)
        print(f"cfgHome_async in axis{axis}: {err}")

        ## Servo on
        err = await dev.Motion_enableServoOn_async(port, axis)
        print(f"enableServoOn_async in axis{axis}: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis, encoder_posi=0)
        print(f"rstEncoderPosi_async in axis{axis}: {err}")

        ## Motion find reference
        err = await dev.Motion_findRef_async(port, axis)
        print(f"findRef_async in axis{axis}: {err}")

        driving_status = 0
        while driving_status == 0:
            ## Read forward and reverse limit status
            hit_status = await dev.Motion_getLimitStatus_async(port, axis)
            forward_hit = hit_status[0]
            reverse_hit = hit_status[1]

            if forward_hit == 1:
                print("Forward hit")
            if reverse_hit == 1:
                print("Reverse hit")

            ## Read home status
            home_status = await dev.Motion_getHomeStatus_async(port, axis)
            if home_status == 1:
                print("Home hit")

            ## Check finding and found status
            driving_status = await dev.Motion_checkRef_async(port, axis)
            print(f"driving_status: {driving_status}")

        ## Motion stop
        err = await dev.Motion_stop_async(port, axis, stop_decel)
        print(f"stop_async in axis{axis}: {err}")

        ## Servo off
        err = await dev.Motion_enableServoOff_async(port, axis)
        print(f"enableServoOff_async in axis{axis}: {err}")

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