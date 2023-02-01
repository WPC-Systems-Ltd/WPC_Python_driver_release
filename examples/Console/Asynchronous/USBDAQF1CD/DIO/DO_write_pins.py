'''
DIO - DO_write_pins.py

This example demonstrates how to write DO in pins from USBDAQF1CD.

First, it shows how to open DO in pins.
Second, write DO pin in two different types (hex or list) but it should be consistency.
Last, close DO in pins.

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

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("21JA1312")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        pin_index = [0,1,2,3,4]

        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output.
        err = await dev.DO_openPins_async(port, pin_index)
        print("DO_openPins_async:", err)

        ## Set pin0, pin1 to high, others to low.
        err = await dev.DO_writePins_async(port, pin_index, [1,1,0,0,0])
        print("DO_writePins_async:", err)

        ## Open pin5, pin6 and pin7 with digital output (1110 0000 in binary) (0xE0 in hex).
        err = await dev.DO_openPins_async(port, 0xE0)
        print("DO_openPins_async:", err)

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        err = await dev.DO_writePins_async(port, 0xE0, 0xC0)
        print("DO_writePins_async:", err)

        ## Wait for 5 second
        await asyncio.sleep(5)  ## delay(second)

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output.
        err = await dev.DO_closePins_async(port, pin_index)
        print("DO_closePins_async:", err)

        ## Close pin5, pin6 and pin7 with digital output.
        err = await dev.DO_closePins_async(port, 0xE0)
        print("DO_closePins_async:", err)
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