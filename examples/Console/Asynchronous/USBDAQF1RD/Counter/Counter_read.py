'''
Counter - Counter_read.py with asynchronous mode.

This example demonstrates how to read counter with USBDAQF1RD.

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
    dev = pywpc.USBDAQF1RD()

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
        channel = 1 ## Depend on your device
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open counter
        err = await dev.Counter_open_async(channel)
        print(f"Counter_open_async in channel {channel}: {err}")

        ## Start counter
        err = await dev.Counter_start_async(channel)
        print(f"Counter_start_async in channel {channel}: {err}")

        ## Read counter
        for i in range(10):
            counter = await dev.Counter_read_async(channel)
            print(f"Read counter in channel {channel}: {counter}")

        ## Stop counter
        err = await dev.Counter_stop_async(channel)
        print(f"Counter_stop_async in channel {channel}: {err}")

        ## Close counter
        err = await dev.Counter_close_async(channel)
        print(f"Counter_close_async in channel {channel}: {err}")
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