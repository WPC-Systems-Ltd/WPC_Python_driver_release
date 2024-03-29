'''
AI - AI_N_samples_once.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in N-sample mode.
Additionally, it gets AI data with points in once from STEM.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
Finally, it concludes by explaining how to close the AI.

If your product is "STEM", please invoke the function `Sys_setAIOMode_async`and `AI_enableCS_async`.
Example: AI_enableCS_async is {0, 2}
Subsequently, the returned value of AI_readOnDemand_async and AI_readStreaming_async will be displayed as follows.
data:
          CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7
          |                                     |                                      |
          |---------------- CS0-----------------|---------------- CS2------------------|
[sample0]
[sample1]
   .
   .
   .
[sampleN]

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.STEM()

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
        slot = 1 ## Connect AIO module to slot
        mode = 1 ## 0 : On demand, 1 : N-samples, 2 : Continuous
        sampling_rate = 1000
        samples = 200
        read_points = 200
        read_delay = 0.5 ## second
        chip_select = [0, 1]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get slot mode
        slot_mode = await dev.Sys_getMode_async(slot)
        print("Slot mode:", slot_mode)

        ## If the slot mode is not set to "AIO", set the slot mode to "AIO"
        if slot_mode != "AIO":
            err = await dev.Sys_setAIOMode_async(slot)
            print(f"Sys_setAIOMode_async in slot {slot}, status: {err}")

        ## Get slot mode
        slot_mode = await dev.Sys_getMode_async(slot)
        print("Slot mode:", slot_mode)

        ## Open AI
        err = await dev.AI_open_async(slot)
        print(f"AI_open_async in slot {slot}, status: {err}")

        ## Enable CS
        err = await dev.AI_enableCS_async(slot, chip_select)
        print(f"AI_enableCS_async in slot {slot}, status: {err}")

        ## Set AI acquisition mode to N-samples mode (1)
        err = await dev.AI_setMode_async(slot, mode)
        print(f"AI_setMode_async {mode} in slot {slot}, status: {err}")

        ## Set AI sampling rate
        err = await dev.AI_setSamplingRate_async(slot, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in slot {slot}, status: {err}")

        ## Set AI # of samples
        err = await dev.AI_setNumSamples_async(slot, samples)
        print(f"AI_setNumSamples_async {samples} in slot {slot}, status: {err}")

        ## Start AI
        err = await dev.AI_start_async(slot)
        print(f"AI_start_async in slot {slot}, status: {err}")

        ## Read AI
        ai_2Dlist = await dev.AI_readStreaming_async(slot, read_points, read_delay)
        print(f"number of samples = {len(ai_2Dlist)}" )

        ok = True
        for i, ai_list in enumerate(ai_2Dlist):
            ## Check for any missing data
            if len(ai_list) != len(chip_select)*8:
                print(i, ai_list)
                ok = False
        if ok:
            print('OK')
        else:
            print('NG')

        ## Stop AI
        err = await dev.AI_stop_async(slot)
        print(f"AI_stop_async in port {slot}, status: {err}")

        ## Close AI
        err = await dev.AI_close_async(slot)
        print(f"AI_close_async in slot {slot}, status: {err}")
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