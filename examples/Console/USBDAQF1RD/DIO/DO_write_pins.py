'''
DIO - DO_write_pins.py

This example demonstrates how to write DO in pins from USBDAQF1RD.

First, it shows how to open DO in pins.
Second, write DO pin in two different types (hex or list) but it should be consistency.
Last, close DO in pins.

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
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("21JA1385")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0
        pin_index = [0,1,2,3,4]

        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output.
        status = await dev.DO_openPins_async(port, pin_index)
        print("DO_openPins_async status: ", status)

        ## Wait for 1 second
        await asyncio.sleep(1)  ## delay(second)

        ## Set pin0, pin1 to high, others to low.
        status = await dev.DO_writePins_async(port, pin_index, [1,1,0,0,0])
        print("DO_writePins_async status: ", status)

        ## Open pin5, pin6 and pin7 with digital output (1110 0000 in binary) (0xE0 in hex).
        status = await dev.DO_openPins_async(port, 0xE0)
        print("DO_openPins_async status: ", status)

        ## Wait for 1 second
        await asyncio.sleep(1)  ## delay(second)

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        status = await dev.DO_writePins_async(port, 0xE0, 0xC0)
        print("DO_writePins_async status: ", status)

        ## Wait for 5 second
        await asyncio.sleep(5)  ## delay(second)

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output.
        status = await dev.DO_closePins_async(port, pin_index)
        print("DO_closePins_async status: ", status)

        ## Close pin5, pin6 and pin7 with digital output.
        status = await dev.DO_closePins_async(port, 0xE0)
        print("DO_closePins_async status: ", status)
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