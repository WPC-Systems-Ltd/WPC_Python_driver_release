'''
AI - AI_N_samples_once.py with asynchronous mode.

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from WifiDAQE3A.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
Last, close AI port.

Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 1 ## Depend on your device
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50
        read_points = 50

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port{port}: {err}")

        ## Set AI port and acquisition mode to N-samples mode (1)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port{port}: {err}")

        ## Set AI port and sampling rate to 1k (Hz)
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in port{port}: {err}")

        ## Set AI port and # of samples to 50 (pts)
        err = await dev.AI_setNumSamples_async(port, samples)
        print(f"AI_setNumSamples_async {samples} in port{port}: {err}")

        ## Set AI port and start acquisition
        err = await dev.AI_start_async(port)
        print(f"AI_start_async in port{port}: {err}")

        ## Wait 1 seconds for acquisition
        await asyncio.sleep(1) ## delay [s]

        ## Set AI port and get 50 points
        data = await dev.AI_readStreaming_async(port, read_points)

        ## Read acquisition data 50 points
        print("Get data points: " + str(len(data)))
        print("Get data: " + str(data))

        ## Close port
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port{port}: {err}")
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