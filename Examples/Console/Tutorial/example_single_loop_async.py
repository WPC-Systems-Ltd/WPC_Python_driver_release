##  example_single_loop_async.py
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

## Python
import asyncio

## WPC
from wpcsys import pywpc

async def loop_func(handle, timeout = 3, delay = 0.5):
    t = 0
    while t < timeout: ## timeout(second)
        data = await handle.Wifi_readRSSI()
        print("RSSI: " + str(data) + " dBm")
        await asyncio.sleep(delay)  ## delay(second)
        t += delay
 
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

    ## Perform async thread to query data
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        await loop_func(dev, 3, 0.5) ## timeout, delay(second)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## This part never execute because the async thread
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__': 
    asyncio.run(main())
