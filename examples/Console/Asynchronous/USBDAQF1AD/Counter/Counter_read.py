'''
Counter - Counter_read.py with asynchronous mode.

This example demonstrates how to read counter with USBDAQF1AD.

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
        channel = 1  ## Depend on your device
        edge = 0  ##  0: Falling edge, 1: Rising edge
        window_size = 100
        position = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open counter
        err = await dev.Counter_open_async(channel)
        print(f"Counter_open_async in channel {channel}, status: {err}")

        ## Set counter edge
        err = await dev.Counter_setEdge_async(channel, edge)
        print(f"Counter_setEdge in channel {channel}, status: {err}")

        ## Set counter frequency window size
        err = await dev.Counter_setFreqWindow_async(channel, window_size)
        print(f"Counter_setFreqWindow in channel {channel}, status: {err}")

        ## Set counter position
        err = await dev.Counter_setPosition_async(channel, position)
        print(f"Counter_setPosition_async in channel {channel}, status: {err}")

        ## Start counter
        err = await dev.Counter_start_async(channel)
        print(f"Counter_start_async in channel {channel}, status: {err}")

        ## Read counter position
        while True:
            posi = await dev.Counter_readPosition_async(channel)
            print(f"Read counter position in channel {channel}: {posi}")
    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop counter
        err = await dev.Counter_stop_async(channel)
        print(f"Counter_stop_async in channel {channel}, status: {err}")

        ## Close counter
        err = await dev.Counter_close_async(channel)
        print(f"Counter_close_async in channel {channel}, status: {err}")

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
