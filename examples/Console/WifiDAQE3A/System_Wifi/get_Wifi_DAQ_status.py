'''
System_Wifi - get_Wifi_DAQ_status.py

This example demonstrates how to get basic information such as RSSI & battery & thermo from WifiDAQE3A.

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
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform to Get RSSI, Battery and Thermo
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get RSSI, battery and thermo
        data1 = await dev.Wifi_readRSSI_async()
        data2 = await dev.Wifi_readBattery_async()
        data3 = await dev.Wifi_readThermo_async()

        print("RSSI: " + str(data1) + " dBm")
        print("Battery: "+ str(data2) + " mV")
        print("Thermo: "+ str(data3) + " °C")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())