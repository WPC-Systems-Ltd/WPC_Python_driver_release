'''
System_USB - get_pin_mode.py

This example demonstrates how to get pin mode from USBDAQF1D.

First, get idle pin mode and show how to open DO and DI in pins.
Second, get idle pin mode and set port idle mode. Again, get pin mode.
Last, close DO and DI in port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples
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
    dev = pywpc.USBDAQF1D()

    ## Connect to device
    try:
        dev.connect("21JA1200")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get pinmode from port 0 to port 3
        for i in range(4):
            ## Get pin mode
            pin_mode = await dev.Sys_getPinModeInPort_async(i)
            print("pin_mode", pin_mode)

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)
            
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