'''
Drive - Drive_velocity_blending_acceleration.py with asynchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
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
        speed = 50000
        dir = 1
        acceleration = 10000
        deceleration = 10000
        active_high = 1
        en_forward = 1
        en_reverse = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"Motion_open, status: {err}")

        ## Motion configure
        err = await dev.Motion_cfgLimit_async(port, en_forward, en_reverse, active_high)
        print(f"Motion_cfgLimit, status: {err}")

        ## Motion reset
        err = await dev.Motion_rstEncoderPosi_async(port)
        print(f"Motion_resetEncoderPosi, status: {err}")

        ## Motion Servo on
        err = await dev.Motion_enableServoOn_async(port)
        print(f"Motion_enableServoOn, status: {err}")

        ## Motion start
        err = await dev.Motion_startVelocticyMove_async(port, speed, dir, acceleration, deceleration)
        print(f"Motion_startVelocticyMove, status: {err}")

        ## Wait for seconds for moving
        await asyncio.sleep(3) ## delay [s]

        ## Motion start
        new_speed = 10000
        new_dir = -1
        new_acceleration = 20000
        new_deceleration = 20000
        err = await dev.Motion_startVelocticyMove_async(port, new_speed, new_dir, new_acceleration, new_deceleration)
        print(f"Motion_startVelocticyMove, status: {err}")

        ## Wait for seconds for moving
        await asyncio.sleep(3) ## delay [s]
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