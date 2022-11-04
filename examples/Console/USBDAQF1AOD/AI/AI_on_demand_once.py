'''
AI - AI_on_demand_once.py

This example demonstrates how to get AI data in on demand mode.
Also, it gets AI data in once with 8 channels from USBDAQF1AOD.

First, it shows how to open AI port.
Second, read AI ondemand data.
Last, close AI port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0
        mode = 0

        ## Open port
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status)

        ## Set AI port and acquisition mode to on demand mode (0)
        status = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async status: ", status)

        ## Set AI port and data acquisition
        data =  await dev.AI_readOnDemand_async(port)
        print("data :" + str(data))

        ## Close port
        status = await dev.AI_close_async(port)
        print("AI_close_async status: ", status)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())