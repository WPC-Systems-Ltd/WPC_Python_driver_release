
'''
AIO - AO_output_while_AI_streaming.py with asynchronous mode.

This example demonstrates the process of AI streaming and AO output from STEM.
Not all of sampling rate can alter the output values of AO.
Its limitation is that the AI sampling rate and the number of CS must be less than or equal to 3000 Hz.

Please invoke the function `Sys_setAIOMode_async` and `AI_enableCS_async`.

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

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio
import random

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
        chip_select = [0, 1]
        mode = 2 ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 200
        read_points = 200
        read_delay = 2 ## second

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

        ## Open AO
        err = await dev.AO_open_async(slot)
        print(f"AO_open_async in slot {slot}, status: {err}")

        ## Open AI
        err = await dev.AI_open_async(slot)
        print(f"AI_open_async in slot {slot}, status: {err}")

        ## Set AI acquisition mode to continuous mode (2)
        err = await dev.AI_setMode_async(slot, mode)
        print(f"AI_setMode_async {mode} in slot {slot}, status: {err}")

        ## Set AI sampling rate
        err = await dev.AI_setSamplingRate_async(slot, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in slot {slot}, status: {err}")

        ## Enable CS
        err = await dev.AI_enableCS_async(slot, chip_select)
        print(f"AI_enableCS_async in slot {slot}, status: {err}")

        ## Open AI streaming
        err = await dev.AI_openStreaming_async(slot)
        print(f"AI_openStreaming_async in slot {slot}, status: {err}")

        ## Start AI streaming
        err = await dev.AI_startStreaming_async(slot)
        print(f"AI_startStreaming_async in slot {slot}, status: {err}")

        counter = 0
        data_len = 1
        ao_list = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        while data_len > 0:
            ## Read data acquisition
            ai_2Dlist = await dev.AI_readStreaming_async(slot, read_points, read_delay)
            # print(ai_2Dlist)
            print(f"Data len = {len(ai_2Dlist)}" )

            ## Update data len and counter
            data_len = len(ai_2Dlist)
            counter+=1

            if counter % 10 == 0:
                ## Select AO random value from AO list
                ao_value = random.choice(ao_list)

                ## Write AO vaule in channel 0
                err = await dev.AO_writeOneChannel_async(slot, 0, ao_value)
                print(f"In slot {slot} channel 0, the AO value is {ao_value}, status: {err}")

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        ## Close AI streaming
        err = await dev.AI_closeStreaming_async(slot)
        print(f"AI_closeStreaming_async in slot {slot}, status: {err}")

        ## Close AI
        err = await dev.AI_close_async(slot)
        print(f"AI_close_async in slot {slot}, status: {err}")

        ## Close AO
        err = await dev.AO_close_async(slot)
        print(f"AO_close_async in slot {slot}, status: {err}")

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
