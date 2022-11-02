
'''
AI - example_AI_continuous_with_logger.py

This example demonstrates how to get AI data in continuous mode and save data into csv file.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels from EthanA.

First, it shows how to open AI port and configure AI parameters.
Second, read and save AI streaming data.
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

async def loop_func(handle, logger_handle, port, num_of_samples = 600, delay = 0.05, timeout = 3):
    t = 0
    while t < timeout:
        ## Data acquisition
        data = await handle.AI_readStreaming_async(port, num_of_samples, delay) ## Get 600 points at a time
        
        if len(data) > 0:
            ## Print data
            print("data :" + str(data))

            ## Write data into CSV file
            logger_handle.Logger_write2DList(data)

        await asyncio.sleep(delay)
        t += delay

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create datalogger handle 
    dev_logger = pywpc.DataLogger()

    ## Open file with WPC_test.csv
    dev_logger.Logger_openFile("WPC_test.csv")

    ## Write header into CSV file
    dev_logger.Logger_writeList(["CH0","CH1","CH2","CH3","CH4","CH5","CH6","CH7"])

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
        mode = 2  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
     
        ## Open port
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status) 

        ## Set AI port and acquisition mode to continuous mode (2)
        status = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async status: ", status)

        ## Set AI port and sampling rate to 1k (Hz)
        status = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print("AI_setSamplingRate_async status: ", status)
        
        ## Wait amount of time (sec)
        await asyncio.sleep(1)

        ## Set AI port and start acquisition
        status = await dev.AI_start_async(port)
        print("AI_start_async status: ", status)

        ## Start async thread
        await loop_func(dev, dev_logger, port, 600, 0.05, 3)

        ## Close port
        status = await dev.AI_close_async(port) 
        print("AI_close_async status: ", status)
        
        ## Close File
        dev_logger.Logger_closeFile()
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