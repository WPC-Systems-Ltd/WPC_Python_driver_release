'''
DIO - DO_blinky_port.py

This example demonstrates how to write DO high or low in port from USBDAQF1AD.

First, it shows how to open DO in port.
Second, each loop has different voltage output so it will look like blinking.
Last, close DO in port.

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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0

        ## Open all pins and set it to digital output.
        err = await dev.DO_openPort_async(port)
        print("DO_openPort_async:", err)

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i%2 == 0:
                value = [0,1,0,1,0,1,0,1]
            else:
                value = [1,0,1,0,1,0,1,0]

            await dev.DO_writePort_async(port, value)
            print(f'Port: {port}, digital state = {value}')
            await asyncio.sleep(0.5)  ## delay(second)

        ## Close all pins with digital output
        err = await dev.DO_closePort_async(port)
        print("DO_closePort_async:", err)
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