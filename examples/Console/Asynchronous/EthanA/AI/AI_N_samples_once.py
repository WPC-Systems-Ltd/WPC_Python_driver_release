'''
AI - AI_N_samples_once.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in N-sample mode.
Additionally, it gets AI data with points in once from EthanA.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
Finally, it concludes by explaining how to close the AI.

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


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanA()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        channel = 8
        mode = 1 ## 0 : On demand, 1 : N-samples, 2 : Continuous
        sampling_rate = 1000
        samples = 200
        read_points = 200
        read_delay = 0.5 ## second

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}: {err}")
        

        ## Set AI acquisition mode to N-samples mode (1)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}: {err}")

        ## Set AI sampling rate
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in port {port}: {err}")

        ## Set AI # of samples
        err = await dev.AI_setNumSamples_async(port, samples)
        print(f"AI_setNumSamples_async {samples} in port {port}: {err}")

        ## Start AI
        err = await dev.AI_start_async(port)
        print(f"AI_start_async in port {port}: {err}")

        ## Read AI
        ai_2Dlist = await dev.AI_readStreaming_async(port, read_points, read_delay)
        print(f"number of samples = {len(ai_2Dlist)}" )

        ok = True
        for i, ai_list in enumerate(ai_2Dlist):
            ## Check for any missing data
            if len(ai_list) != channel:
                print(i, ai_list)
                ok = False
        if ok:
            print('OK')
        else:
            print('NG')

        ## Stop AI
        err = await dev.AI_stop_async(port)
        print(f"AI_stop_async in port {port}: {err}")

        ## Close AI
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