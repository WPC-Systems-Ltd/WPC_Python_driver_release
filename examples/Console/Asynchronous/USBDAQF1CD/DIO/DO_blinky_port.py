'''
DIO - DO_blinky_port.py with asynchronous mode.

This example demonstrates how to write DO high or low in port from USBDAQF1CD.

First, it shows how to open DO in port.
Second, each loop has different voltage output so it will look like blinking.
Last, close DO in port.

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
    dev = pywpc.USBDAQF1CD()

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
        port = 0 ## Depend on your device

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open all pins and set it to digital output.
        err = await dev.DO_openPort_async(port)
        print(f"DO_openPort_async in port{port}: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i%2 == 0:
                value = [0,1,0,1,0,1,0,1]
            else:
                value = [1,0,1,0,1,0,1,0]

            await dev.DO_writePort_async(port, value)
            print(f'Port: {port}, digital state= {value}')

            ## Wait for 0.5 second to see led status
            await asyncio.sleep(0.5)  ## delay [s]

        ## Close all pins with digital output
        err = await dev.DO_closePort_async(port)
        print(f"DO_closePort_async in port{port}: {err}")
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