'''
System - example_get_device_info.py

This example demonstrates how to get hardware & network information from WPC-Wifi-DAQ-E3-A.

First, get hardware information such as firmware model & version & serial number.
Last, get network information such as IP & submask & mac.

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
    dev = pywpc.WifiDAQE3A()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform DAQ basic information 
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
 
        ## Get serial number & RTC Time
        print(f'Serial number = ' + await dev.Sys_getSerialNumber_async())
        print(f'RTC data time = ' + await dev.Sys_getRTC_async())

        ## Get IP & submask & MAC
        ip_addr, submask = await dev.Sys_getIPAddrAndSubmask_async()
        print(f'IP = ' + ip_addr)
        print(f'Submask = '+ submask)
        print(f'MAC = ' + await dev.Sys_getMACAddr_async())
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
