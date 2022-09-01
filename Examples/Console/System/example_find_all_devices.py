'''
System - example_find_all_devices.py

This example demonstrates how to find all available Wifi or ethernet device. 

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
    dev = pywpc.Broadcaster()

    ## Connect to network device
    try:
        dev.connect()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform device information
    try:
        print(f'Broadcast -' + str(await dev.Bcst_getDeviceInfo()))
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
