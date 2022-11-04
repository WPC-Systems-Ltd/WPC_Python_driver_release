'''
Tutorial - multiple_loops_thread.py

This example project demonstrates how to use two thread to get RTC & print string from USBDAQF1AD.

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

async def printString(handle, delay = 1):
    print("WPC Systems Ltd")
    await asyncio.sleep(delay)  # delay(second)

def RTC_thread(handle, delay):
    while True:
        asyncio.run(getRTC(handle, delay))
        time.sleep(1)

def Print_thread(handle, delay):
    while True:
        asyncio.run(printString(handle, delay))
        time.sleep(1)

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform two sync thread to query data
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        _threadPrint = threading.Thread(target = Print_thread, args=[dev, 1])
        _threadPrint.start()

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