'''
PWM - PWM_generate.py with asynchronous mode.

This example demonstrates how to generate PWM with USBDAQF1AD.

First, you should set frequency and duty cycle so that it can generate proper signal.
By the way, if you want to check PWM signal, you could connect DI pin with PWM pin.

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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        channel = 0  ## Depend on your device
        frequency = 100
        duty_cycle = 50

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open PWM
        err = await dev.PWM_open_async(channel)
        print(f"PWM_open_async in channel {channel}, status: {err}")

        ## Set frequency
        err = await dev.PWM_setFrequency_async(channel, frequency)
        print(f"PWM_setFrequency_async in channel {channel}, status: {err}")

        ## Set duty cycle
        err = await dev.PWM_setDutyCycle_async(channel, duty_cycle)
        print(f"PWM_setDutyCycle_async in channel {channel}, status: {err}")

        ## Start PWM
        err = await dev.PWM_start_async(channel)
        print(f"PWM_start_async in channel {channel}, status: {err}")

        ## Wait for seconds for generating signal
        await asyncio.sleep(5)  ## delay [sec]

        ## Stop PWM
        err = await dev.PWM_stop_async(channel)
        print(f"PWM_stop_async in channel {channel}, status: {err}")

        ## Close PWM
        err = await dev.PWM_close_async(channel)
        print(f"PWM_close_async in channel {channel}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
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
