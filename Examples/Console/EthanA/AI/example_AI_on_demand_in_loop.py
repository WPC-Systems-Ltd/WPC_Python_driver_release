
'''
AI - example_AI_on_demand_in_loop.py

This example demonstrates how to get AI data in on demand mode.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels EthanA.

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

## WPC
from wpcsys import pywpc

async def loop_func(handle, port, delay, timeout = 3):
    t = 0
    while t < timeout:
        ## data acquisition
        data =  await handle.AI_readOnDemand_async(port)
        print("data :" + str(data))
        await asyncio.sleep(delay)
        t += delay

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanA()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0
        mode = 0
        
        ## Open port
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status)
 
        ## Set AI port and start async thread
        await loop_func(dev, port, 1, 3)
    
        ## Set AI port and acquisition mode to on demand mode (0)
        status = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async status: ", status)
        
        ## Close port
        status = await dev.AI_close_async(port) 
        print("AI_close_async status: ", status)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Disconnect device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return
    
if __name__ == '__main__':
    asyncio.run(main())