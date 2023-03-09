'''
DIO - DO_write_port.py with asynchronous mode.

This example demonstrates how to write DO in port from EthanD.

First, it shows how to open DO in port.
Second, write DO pins in two different types (hex or list) but it should be consistency.
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
    dev = pywpc.EthanD()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0 ## Depend on your device

        ## Open all pins and set it to digital output
        err = await dev.DO_openPort_async(port)
        print(f"DO_openPort_async in port{port}: {err}")

        ## Set pin0, pin3 and pin4 to high, others to low
        err = await dev.DO_writePort_async(port, [0,0,0,1,1,0,0,1])
        print(f"DO_writePort_async in port{port}: {err}")

        ## Wait for 1 seconds to see led status
        await asyncio.sleep(1)  ## delay [s]

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        err = await dev.DO_writePort_async(port, 0xC0)
        print(f"DO_writePort_async in port{port}: {err}")

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