'''
Temperature_RTD - RTD_read_channel_data.py

This example demonstrates how to read RTD data in two channels from USBDAQF1RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data
Last, close thermal port.

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
        port = 1
        channel_0 = 0
        channel_1 = 1

        ## Open RTD
        status = await dev.Thermal_open_async(port)
        print("Thermal_open_async status: ", status)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set RTD port and read RTD in channel 0
        data0 = await dev.Thermal_readSensor_async(port, channel_0)
        print("Read channel 0 data:", data0, "°C")

        ## Set RTD port and read RTD in channel 1
        data1 = await dev.Thermal_readSensor_async(port, channel_1)
        print("Read channel 1 data:", data1, "°C")

        ## Close RTD
        status = await dev.Thermal_close_async(port)
        print("Thermal_close_async status: ", status)
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