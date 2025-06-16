'''
Temperature_RTD - RTD_read_channel_data_with_logger.py with asynchronous mode.

This example demonstrates how to read RTD data in two channels and save data into csv file from USBDAQF1RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data and save them.
Last, close thermal port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc

## Python
import asyncio
import sys
sys.path.insert(0, 'src/')


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 1  ## Depend on your device
        ch0 = 0
        ch1 = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open file with WPC_test.csv
        err = dev.Logger_openFile("WPC_test.csv")
        print(f"Logger_openFile, status: {err}")

        ## Write header into CSV file
        err = dev.Logger_writeHeader(["RTD CH0", "RTD CH1"])
        print(f"Logger_writeHeader, status: {err}")

        ## Open RTD
        err = await dev.Thermal_open_async(port)
        print(f"Thermal_open_async in port {port}, status: {err}")

        ## Wait for at least 100 ms
        await asyncio.sleep(0.1)  ## delay [sec]

        ## Set RTD port and read RTD in channel 0
        data0 = await dev.Thermal_readSensor_async(port, ch0)
        print(f"Read sensor in channel {ch0} in port {port}: {data0} deg C")

        ## Set RTD port and read RTD in channel 1
        data1 = await dev.Thermal_readSensor_async(port, ch1)
        print(f"Read sensor in channel {ch1} in port {port}: {data1} deg C")

        ## Write data into CSV file
        err = dev.Logger_writeList([data0, data1])
        print(f"Logger_writeList, status: {err}")

        ## Close RTD
        err = await dev.Thermal_close_async(port)
        print(f"Thermal_close_async in port {port}, status: {err}")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
