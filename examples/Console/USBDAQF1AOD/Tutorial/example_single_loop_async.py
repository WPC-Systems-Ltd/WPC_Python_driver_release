
'''
Tutorial - example_single_loop_async.py

This example project demonstrates how to use async thread to get RTC from USBDAQF1AOD.

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

async def loop_func(handle, timeout = 3, delay = 1):
    t = 0
    while t < timeout: ## timeout(second)
        data = await handle.Sys_getRTC_async()
        print("RTC Time: " + str(data))
        await asyncio.sleep(delay)  ## delay(second)
        t += delay
 
async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)
    ## Perform async thread to query data
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        await loop_func(dev, 3, 1) ## timeout, delay(second)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## This part never execute because the async thread
    ## Disconnect device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__': 
    asyncio.run(main())