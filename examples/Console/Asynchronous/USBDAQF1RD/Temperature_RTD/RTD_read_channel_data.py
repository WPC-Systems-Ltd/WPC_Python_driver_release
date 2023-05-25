'''
Temperature_RTD - RTD_read_channel_data.py with asynchronous mode.

This example demonstrates how to read RTD data in two channels from USBDAQF1RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data
Last, close thermal port.

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
    dev = pywpc.USBDAQF1RD()

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
        port = 1 ## Depend on your device
        ch0 = 0
        ch1 = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open RTD
        err = await dev.Thermal_open_async(port)
        print(f"Thermal_open_async in port {port}: {err}")

        ## Wait for at least 100 ms
        await asyncio.sleep(0.1) ## delay [s]

        ## Set RTD port and read RTD in channel 0
        data0 = await dev.Thermal_readSensor_async(port, ch0)
        print(f"Read sensor in channel {ch0} in port {port}: {data0}°C")

        ## Set RTD port and read RTD in channel 1
        data1 = await dev.Thermal_readSensor_async(port, ch1)
        print(f"Read sensor in channel {ch1} in port {port}: {data1}°C")

        ## Close RTD
        err = await dev.Thermal_close_async(port)
        print(f"Thermal_close_async in port {port}: {err}")
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