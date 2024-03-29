'''
Drive - Drive_position_blending.py with asynchronous mode.

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
    dev = pywpc.EDriveST()

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
        position = 10000
        position1 = 30000
        position2 = -10000
        speed = 10000
        acceleration = 10000
        deceleration = 10000
        mode = 1    ## 0: absolute, 1: relative.
        active_low = 0
        active_high = 1
        en_forward = 0
        en_reverse = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"Motion_open: {err}")

        ## Motion configure
        err = await dev.Motion_cfgLimit_async(port, en_forward, en_reverse, active_low)
        print(f"Motion_cfgLimit: {err}")

        ## Motion reset
        err = await dev.Motion_rstEncoderPosi_async(port)
        print(f"Motion_resetEncoder: {err}")

        ## Motion Servo on
        err = await dev.Motion_enableServoOn_async(port)
        print(f"Motion_enableServoOn: {err}")

        ## Motion start
        err = await dev.Motion_startPositionMove_async(port, position, speed, acceleration, deceleration, mode)
        print(f"Motion_startPositionMove: {err}")

        ## Wait for seconds for moving
        await asyncio.sleep(1) ## delay [s]

        ## Motion start
        err = await dev.Motion_startPositionMove_async(port, position1, speed, acceleration, deceleration, mode)
        print(f"Motion_startPositionMove: {err}")

        ## Wait for seconds for moving
        await asyncio.sleep(1) ## delay [s]

        ## Motion start
        err = await dev.Motion_startPositionMove_async(port, position2, speed, acceleration, deceleration, mode)
        print(f"Motion_startPositionMove: {err}")

        status = 1
        while status != 0 :
            status = await dev.Motion_getProcessState_async(port)

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        ## Motion stop
        err = await dev.Motion_stopProcess_async(port)
        print(f"Motion_stopProcess: {err}")

        ## Motion Servo off
        err = await dev.Motion_enableServoOff_async(port)
        print(f"Motion_enableServoOff: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"Motion_close: {err}")

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
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder