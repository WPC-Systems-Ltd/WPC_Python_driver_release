'''
AI - AI_N_samples_once.py

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from USBDAQF1AOD.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
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

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50
        read_points = 50

        ## Open port
        err = await dev.AI_open_async(port)
        print("AI_open_async:", err)

        ## Set AI port and acquisition mode to N-samples mode (1)
        err = await dev.AI_setMode_async(port, mode)
        print("AI_setMode_async:", err)

        ## Set AI port and sampling rate to 1k (Hz)
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print("AI_setSamplingRate_async:", err)

        ## Set AI port and # of samples to 50 (pts)
        err = await dev.AI_setNumSamples_async(port, samples)
        print("AI_setNumSamples_async:", err)

        ## Set AI port and start acquisition
        err = await dev.AI_start_async(port)
        print("AI_start_async:", err)

        ## Wait amount of time (sec)
        await asyncio.sleep(1)

        ## Set AI port and get 50 points
        data = await dev.AI_readStreaming_async(port, read_points)

        ## Read acquisition data 50 points
        print("Get data points:" + str(len(data)))
        print("Get data:" + str(data))

        ## Close port
        err = await dev.AI_close_async(port)
        print("AI_close_async:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return

if __name__ == '__main__':
    asyncio.run(main())