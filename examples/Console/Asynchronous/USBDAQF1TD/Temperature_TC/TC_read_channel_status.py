'''
Temperature_TC - TC_read_channel_status.py with asynchronous mode.

This example demonstrates how to get status from USBDAQF1TD.

First, it shows how to open thermal port
Second, get status from channel 0 and channel 1
Last, close thermal port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

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

        ## Open thermo
        err = await dev.Thermal_open_async(port)
        print(f"Thermal_open_async in port {port}, status: {err}")

        ## Set thermo port and get status in channel 0
        status = await dev.Thermal_getStatus_async(port, ch0)
        print(f"Thermal_getStatus_async in channel {ch0} in port {port}: {status}")

        ## Set thermo port and get status in channel 1
        status = await dev.Thermal_getStatus_async(port, ch1)
        print(f"Thermal_getStatus_async in channel {ch1} in port {port}: {status}")

        ## Close thermo
        err = await dev.Thermal_close_async(port)
        print(f"Thermal_close_async in port {port}, status: {err}")
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