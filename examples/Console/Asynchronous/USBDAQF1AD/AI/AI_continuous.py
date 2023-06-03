'''
AI - AI_continuous.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode.
Additionally, it utilizes a loop to retrieve AI data with 8 channels from USBDAQF1AD with a timeout of 100 ms.

To begin with, it demonstrates the steps to open the AI port and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
Finally, it concludes by explaining how to close the AI port.

-------------------------------------------------------------------------------------
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

async def loop_func(handle, port, num_of_samples=600, delay=0.05, exit_loop_time=3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## Read data acquisition
        data = await handle.AI_readStreaming_async(port, num_of_samples, delay=delay) ## Get 600 points at a time

        ## Print data
        for i in range(len(data)):
            print(f"{data[i]}")

        ## Wait
        await asyncio.sleep(delay)  ## delay [s]
        time_cal += delay

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        mode = 2  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        chip_select = [0, 1]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Open port
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}: {err}")
        

        ## Set AI acquisition mode to continuous mode (2)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}: {err}")

        ## Set AI sampling rate to 1k (Hz)
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in port {port}: {err}")

        ## Start AI acquisition
        err = await dev.AI_start_async(port)
        print(f"AI_start_async in port {port}: {err}")

        ## Wait 1 seconds for acquisition
        await asyncio.sleep(1) ## delay [s]

        ## Set loop parameters
        num_of_samples = 100
        delay = 0.05
        exit_loop_time = 0.1

        ## Start loop
        await loop_func(dev, port, num_of_samples=num_of_samples, delay=delay, exit_loop_time=exit_loop_time)

        ## Close port
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}: {err}")
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