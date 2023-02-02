'''
AI - AI_continuous_with_logger.py

This example demonstrates how to get AI data in continuous mode and save data into csv file.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels from WifiDAQE3A.

First, it shows how to open AI port and configure AI parameters.
Second, read and save AI streaming data.
Last, close AI port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def loop_func(handle, logger_handle, port, num_of_samples = 600, delay = 0.05, exit_loop_time = 3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## Data acquisition
        data = await handle.AI_readStreaming_async(port, num_of_samples, delay) ## Get 600 points at a time

        if len(data) > 0:
            ## Print data
            print("data :" + str(data))

            ## Write data into CSV file
            logger_handle.Logger_write2DList(data)

        await asyncio.sleep(delay)
        time_cal += delay

async def main(): 
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create datalogger handle
    dev_logger = pywpc.DataLogger()

    ## Open file with WPC_test.csv
    dev_logger.Logger_openFile("WPC_test.csv")

    ## Write header into CSV file
    dev_logger.Logger_writeList(["CH0","CH1","CH2","CH3","CH4","CH5","CH6","CH7"])

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        mode = 2  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000

        ## Open port
        err = await dev.AI_open_async(port)
        print("AI_open_async:", err)

        ## Set AI port and acquisition mode to continuous mode (2)
        err = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async:", err)

        ## Set AI port and sampling rate to 1k (Hz)
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print("AI_setSamplingRate_async:", err)

        ## Set AI port and start acquisition
        err = await dev.AI_start_async(port)
        print("AI_start_async:", err)

        ## Start async thread
        num_of_samples = 600
        delay = 0.05
        exit_loop_time = 3
        
        await loop_func(dev, dev_logger, port, num_of_samples, delay, exit_loop_time)

        ## Close port
        err = await dev.AI_close_async(port)
        print("AI_close_async:", err)

        ## Close File
        dev_logger.Logger_closeFile()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))
 
if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder
 