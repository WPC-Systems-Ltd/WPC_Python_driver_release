'''
DIO - DIO_loopback_port.py

This example demonstrates how to write DIO loopback in port from EthanD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
Last, close DO and DI in port.

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
    dev = pywpc.EthanD()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port_DO = 0
        port_DI = 1

        ## Open all pins with digital output
        err = await dev.DO_openPort_async(port_DO)
        print("DO_openPort_async:", err)

        ## Open all pins with digital input
        err = await dev.DI_openPort_async(port_DI)
        print("DI_openPort_async:", err)

        ## Set pin0, pin1 and pin2 to high, others to low
        err = await dev.DO_writePort_async(port_DO, [0,0,0,1,0,0,0,0])
        print("DO_writePort_async:", err)

        ## Read all pins state
        state_list = await dev.DI_readPort_async(port_DI)
        print(state_list)

        ## Wait for 1 seconds
        await asyncio.sleep(1)

        ## Close all pins with digital output
        err = await dev.DO_closePort_async(port_DO)
        print("DO_closePort_async:", err)

        ## Close all pins with digital input
        err = await dev.DI_closePort_async(port_DI)
        print("DI_closePort_async:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return

if __name__ == '__main__':
    asyncio.run(main())