'''
Drive - Drive_find_limit.py with asynchronous mode.

-------------------------------------------------------------------------------------
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
    dev = pywpc.EDrive_ST()

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
        forward = 0
        reverse = 1
        orginal_direction = 0

        ## Operation and stop mode
        stop_decel = 0
        timeout = 3  ## second

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        en_forward = 0
        en_reverse = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## EDrive-ST open
        err = await dev.Drive_open_async(port)
        print(f"Drive_open: {err}")

        ## EDrive-ST configure
        err = await dev.Drive_cfgAxisDirection_async(port, orginal_direction)
        print(f"Drive_cfgAxisDirection: {err}")

        err = await dev.Drive_cfgEncoderDirection_async(port, orginal_direction)
        print(f"Drive_cfgEncoderDirection: {err}")

        err = await dev.Drive_cfgLimit_async(port, en_forward, en_reverse, active_low)
        print(f"Drive_cfgLimit: {err}")

        err = await dev.Drive_cfgFindRef_async(port, reverse)
        print(f"Drive_cfgFindRef: {err}")

        ## EDrive-ST reset
        err = await dev.Drive_rstEncoderPosi_async(port)
        print(f"EDST_reset: {err}")

        ## EDrive-ST Servo on
        err = await dev.Drive_enableServoOn_async(port)
        print(f"Drive_enableServoOn: {err}")

        ## EDrive-ST find reference
        err = await dev.Drive_findReference_async(port)
        print(f"Drive_findReference: {err}")

        ## Get limit status
        limit_status = await dev.Drive_getLimitStatus_async(port)
        reverse_hit = limit_status[0]
        forward_hit = limit_status[1]
        print("reverse_hit: ", reverse_hit)
        print("forward_hit: ", forward_hit)

        ## Wait for 3 seconds for moving
        await asyncio.sleep(3) ## delay [s]

        ## EDrive-ST Stop
        err = await dev.Drive_stop_async(port, stop_decel)
        print(f"Drive_stop: {err}")

        ## EDrive-ST Servo off
        err = await dev.Drive_enableServoOff_async(port)
        print(f"Drive_enableServoOff: {err}")

        ## EDrive-ST close
        err = await dev.Drive_close_async(port)
        print(f"Drive_close: {err}")
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