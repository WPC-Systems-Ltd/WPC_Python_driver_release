 
'''
Tutorial - example_single_loop_thread.py

This example project demonstrates how to use thread to get RTC from USBDAQF1CD.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio
import threading
import time
 
## WPC 
 
from wpcsys import pywpc 

async def getRTC(handle, delay = 1):
    data = await handle.Sys_getRTC_async()
    print("RTC Time: " + str(data))
    await asyncio.sleep(delay)  ## delay(second)

def RTC_thread(handle, delay = 1):
    while True:
        asyncio.run(getRTC(handle, delay))
        time.sleep(delay)

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("21JA1320")
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Perform two sync thread to query data
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        _threadRTC = threading.Thread(target = RTC_thread, args=[dev, 1])
        _threadRTC.start()
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## This part will execute immediately because the sync thread is running in parallel.
    '''
    # Disconnect device
    dev.disconnect()
    
    # Release device handle
    dev.close()
    '''

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())