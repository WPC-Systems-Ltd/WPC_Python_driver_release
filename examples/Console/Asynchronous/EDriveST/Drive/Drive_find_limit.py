'''
Drive - Drive_find_limit.py with asynchronous mode.

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
    dev = pywpc.EDriveST()

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
        mode = 1  ## 1: forward, -1: reverse.
        active_high = 1
        en_forward = 1
        en_reverse = 1
        searching_speed = 50000
        approaching_speed = 10000
        acceleration = 10000
        offset = 0
        reset_position = False

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"Motion_open, status: {err}")

        ## Motion config
        err = await dev.Motion_cfgLimit_async(port, en_forward, en_reverse, active_high)
        print(f"Motion_cfgLimit, status: {err}")

        ## Motion reset
        err = await dev.Motion_rstEncoderPosi_async(port)
        print(f"Motion_resetEncoder, status: {err}")

        ## Motion Servo on
        err = await dev.Motion_enableServoOn_async(port)
        print(f"Motion_enableServoOn, status: {err}")

        ## Motion find reference
        err = await dev.Motion_startFindLimit_async(port, mode, searching_speed, approaching_speed, acceleration, offset, reset_position)
        print(f"Motion_startFindLimit, status: {err}")

        status = 1
        while status != 0:
            status = await dev.Motion_getProcessState_async(port)
            if status == 0:
                print(f"Motion_getProcessState: {status}")

        ## Motion get limit status
        state_list = await dev.Motion_getLimitStatus_async(port)
        print(f"Forward limit status: {state_list[0]}")
        print(f"Reverse limit status: {state_list[1]}")
        print(f"Home status: {state_list[2]}")

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        ## Motion stop
        err = await dev.Motion_stopProcess_async(port)
        print(f"Motion_stopProcess, status: {err}")

        ## Motion Servo off
        err = await dev.Motion_enableServoOff_async(port)
        print(f"Motion_enableServoOff, status: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"Motion_close, status: {err}")

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
