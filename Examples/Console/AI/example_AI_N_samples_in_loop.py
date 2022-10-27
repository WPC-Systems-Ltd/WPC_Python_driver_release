'''
AI - example_AI_N_samples_in_loop.py

This example demonstrates how to get AI data in N samples mode.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels from Wifi-DAQ-E3-A.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
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

async def loop_func(handle, port, num_of_samples = 600, delay = 0.005, timeout = 3):
    t = 0
    while t < timeout:
        ## data acquisition
        data = await handle.AI_readStreaming_async(port, num_of_samples, delay)
        if data is not None:
            print(data)
            print("Get data points: " + str(len(data)))
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
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 1
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 5000
        samples = 3000

        ## Open port 1
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status)

        ## Set AI port to 1 and acquisition mode to N-samples mode (1)
        status = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async status: ", status)

        ## Set AI port to 1 and set sampling rate to 5k (Hz)
        status = await dev.AI_setSamplingRate_async(port, sampling_rate) 
        print("AI_setSamplingRate_async status: ", status)

        ## Set AI port to 1 and # of samples to 3000 (pts)
        status = await dev.AI_setNumSamples_async(port, samples) 
        print("AI_setNumSamples_async status: ", status)

        ## Set AI port to 1 and start acquisition
        status = await dev.AI_start_async(port)
        print("AI_start_async status: ", status)

        ## Start async thread
        await loop_func(dev, port, 600, 0.005, 3)

        ## Close port 1
        status = await dev.AI_close_async(port) 
        print("AI_close_async status: ", status)
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