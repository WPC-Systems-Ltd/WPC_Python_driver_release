'''
AI - AI_N_samples_once.py

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from USBDAQF1AD.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
Last, close AI port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50
        read_points = 50

        ## Open port
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status)

        ## Set AI port and acquisition mode to N-samples mode (1)
        status = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async status: ", status)

        ## Set AI port and sampling rate to 1k (Hz)
        status = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print("AI_setSamplingRate_async status: ", status)

        ## Set AI port and # of samples to 50 (pts)
        status = await dev.AI_setNumSamples_async(port, samples)
        print("AI_setNumSamples_async status: ", status)

        ## Set AI port and start acquisition
        status = await dev.AI_start_async(port)
        print("AI_start_async status: ", status)

        ## Wait amount of time (sec)
        await asyncio.sleep(1)

        ## Set AI port and get 50 points
        data = await dev.AI_readStreaming_async(port, read_points)

        ## Read acquisition data 50 points
        print("Get data points: " + str(len(data)))
        print("Get data: " + str(data))

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