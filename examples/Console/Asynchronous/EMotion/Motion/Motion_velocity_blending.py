'''
Motion - Motion_velocity_blending.py with asynchronous mode.

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
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0 ## Depend on your device
        axis = 0
        two_pulse_mode = 1
        velocity_mode = 2
        stop_decel = 0
        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0
        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"open_async in port{port}: {err}")

        ## Motion configure
        err = await dev.Motion_cfgAxis_async(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print(f"cfgAxis_async in port{port}: {err}")

        err = await dev.Motion_cfgLimit_async(port, axis, forward_enable_true, reverse_enable_true, active_high)
        print(f"cfgLimit_async in port{port}: {err}")

        err = await dev.Motion_cfgEncoder_async(port, axis, active_low)
        print(f"cfgEncoder_async in port{port}: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis)
        print(f"rstEncoderPosi_async in port{port}: {err}")

        err = await dev.Motion_cfgAxisMove_async(port, axis, velocity_mode, velocity = 1000)
        print(f"cfgAxisMove_async in port{port}: {err}")

        err = await dev.Motion_enableServoOn_async(port, axis, int(True))
        print(f"enableServoOn_async in port{port}: {err}")

        ## Motion start
        err = await dev.Motion_startSingleAxisMove_async(port, axis)
        print(f"startSingleAxisMove_async in port{port}: {err}")

        await asyncio.sleep(3)

        ## Motion override velocity
        new_velo = 5000
        err = await dev.Motion_overrideAxisVelocity_async(port, axis, new_velo)
        print(f"overrideAxisVelocity_async in port{port}: {err}")

        await asyncio.sleep(3)

        ## Motion override velocity
        new_velo = -3000
        err = await dev.Motion_overrideAxisVelocity_async(port, axis, new_velo)
        print(f"overrideAxisVelocity_async in port{port}: {err}")

        await asyncio.sleep(3)

        ## Motion stop
        err = await dev.Motion_stop_async(port, axis, stop_decel)
        print(f"stop_async in port{port}: {err}")

        err = await dev.Motion_enableServoOn_async(port, axis, int(False))
        print(f"enableServoOn_async in port{port}: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"close_async in port{port}: {err}")

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