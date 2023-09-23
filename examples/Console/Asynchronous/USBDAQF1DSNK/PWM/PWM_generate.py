'''
PWM - PWM_generate.py with asynchronous mode.

This example demonstrates how to generate PWM with USBDAQF1DSNK.

First, you should set frequency and duty cycle so that it can generate proper signal.
By the way, if you want to check PWM signal, you could connect DI pin with PWM pin.

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
    dev = pywpc.USBDAQF1DSNK()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        channel = 0 ## Depend on your device
        frequency = 100
        duty_cycle = 50
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open PWM
        err = await dev.PWM_open_async(channel)
        print(f"PWM_open_async in channel {channel}: {err}")

        ## Set frequency and duty_cycle
        err = await dev.PWM_setFrequency_async(channel, frequency)
        print(f"PWM_setFrequency_async in channel {channel}: {err}")

        err = await dev.PWM_setDutyCycle_async(channel, duty_cycle)
        print(f"PWM_setDutyCycle_async in channel {channel}: {err}")

        ## Start PWM
        err = await dev.PWM_start_async(channel)
        print(f"PWM_start_async in channel {channel}: {err}")

        ## delay for 5 seconds
        time.sleep(5)

        ## Stop PWM
        err = await dev.PWM_stop_async(channel)
        print(f"PWM_stop_async in channel {channel}: {err}")

        ## Close PWM
        err = await dev.PWM_close_async(channel)
        print(f"PWM_close_async in channel {channel}: {err}")
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