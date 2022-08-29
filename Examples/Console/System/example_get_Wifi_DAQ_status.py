'''
System - example_get_Wifi_DAQ_status.py

Get RSSI & Battery & Thermo data with Wifi-DAQ-E3-A.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio
import sys
 
## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform to Get RSSI, Battery and Thermo
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get RSSI, battery and thermo
        data1 = await dev.Wifi_readRSSI()
        data2 = await dev.Wifi_readBattery()
        data3 = await dev.Wifi_readThermo()

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
