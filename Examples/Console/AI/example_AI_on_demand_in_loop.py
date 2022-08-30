'''
AI - example_AI_on_demand_in_loop.py

This example demonstrates how to get AI data in on demand mode.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels from Wifi-DAQ-E3-A.

First, it shows how to open AI port and configure AI parameters.
Second, read AI ondemand data.
Last, close AI port.

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

async def loop_func(handle, port, delay, timeout = 3):
    t = 0
    while t < timeout:
        ## data acquisition
        data =  await handle.AI_readOnDemand(port)
        print("data :" + str(data))
        await asyncio.sleep(delay)
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

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 1

        ## Open port 1
        status = await dev.AI_open(port)
        if status == 0: print("AI_open: OK") 
 
        ## Set AI port to 1 and start async thread
        await loop_func(dev, port, 1, 3)
    
        ## Close port 1
        status = await dev.AI_close(port) 
        if status == 0: print("AI_close: OK")
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