'''
Encoder - Encoder_read.py with asynchronous mode.

This example demonstrates how to read encoder with USBDAQF1AOD.

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
    dev = pywpc.USBDAQF1AOD()

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
        direction = 1  ## 1 : Forward, -1 : Reverse
        position = 0
        window_size = 100

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open encoder
        err = await dev.Encoder_open_async(channel)
        print(f"Encoder_open_async in channel {channel}, status: {err}")

        ## Set encoder direction
        err = await dev.Encoder_setDirection_async(channel, direction)
        print(f"Encoder_setDirection_async in channel {channel}, status: {err}")

        ## Set encoder position
        err = await dev.Encoder_setPosition_async(channel, position)
        print(f"Encoder_setPosition_async in channel {channel}, status: {err}")

        ## Set encoder frequency window size
        err = await dev.Encoder_setFreqWindow_async(channel, window_size)
        print(f"Encoder_setFreqWindow_async in channel {channel}, status: {err}")

        ## Start encoder
        err = await dev.Encoder_start_async(channel)
        print(f"Encoder_start_async in channel {channel}, status: {err}")

        ## Read encoder position
        while True:
            posi = await dev.Encoder_readPosition_async(channel)
            print(f"Encoder position in channel {channel}: {posi}")
    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop encoder
        err = await dev.Encoder_stop_async(channel)
        print(f"Encoder_stop_async in channel {channel}, status: {err}")

        ## Close encoder
        err = await dev.Encoder_close_async(channel)
        print(f"Encoder_close_async in channel {channel}, status: {err}")

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