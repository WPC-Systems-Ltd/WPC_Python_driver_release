'''
Temperature_RTD - RTD_read_channel_status.py with asynchronous mode.

This example demonstrates how to get status in two channels from USBDAQF1RD.

First, it shows how to open thermal port
Second, get status from channel 0 and channel 1
Last, close thermal port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main(): 
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("21JA1385")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        channel_0 = 0
        channel_1 = 1

        ## Open RTD
        err = await dev.Thermal_open_async(port)
        print("Thermal_open_async:", err)

        ## Set RTD port and get status in channel 0
        status = await dev.Thermal_getStatus_async(port, channel_0)
        print("Thermal_getStatus_async status in channel_0:", status)

        ## Set RTD port and get status in channel 1
        status = await dev.Thermal_getStatus_async(port, channel_1)
        print("Thermal_getStatus_async status in channel_1:", status)

        ## Close RTD
        err = await dev.Thermal_close_async(port)
        print("Thermal_close_async:", err)
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