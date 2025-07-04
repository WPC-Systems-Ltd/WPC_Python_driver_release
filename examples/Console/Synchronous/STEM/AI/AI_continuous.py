'''
AI - AI_continuous.py with synchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode with 8 channels from STEM.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
Finally, it concludes by explaining how to close the AI.

If your product is "STEM", please invoke the function `Sys_setAIOMode`and `AI_enableCS`.
Example: AI_enableCS is {0, 2}
Subsequently, the returned value of AI_readOnDemand and AI_readStreaming will be displayed as follows.
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

## WPC
from wpcsys import pywpc

## Python
import time


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.STEM()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        slot = 1  ## Connect AIO module to slot
        mode = 2  ## 0: On demand, 1: N-samples, 2: Continuous
        sampling_rate = 200
        read_points = 200
        read_delay = 0.2  ## [sec]
        timeout = 3  ## [sec]
        chip_select = [0, 1]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout)
        print("Slot mode:", slot_mode)

        ## If the slot mode is not set to "AIO", set the slot mode to "AIO"
        if slot_mode != "AIO":
            err = dev.Sys_setAIOMode(slot, timeout)
            print(f"Sys_setAIOMode in slot {slot}, status: {err}")

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout)
        print("Slot mode:", slot_mode)

        ## Open AI
        err = dev.AI_open(slot, timeout)
        print(f"AI_open in slot {slot}, status: {err}")

        ## Enable CS
        err = dev.AI_enableCS(slot, chip_select, timeout)
        print(f"AI_enableCS in slot {slot}, status: {err}")

        ## Set AI acquisition mode to continuous mode (2)
        err = dev.AI_setMode(slot, mode, timeout)
        print(f"AI_setMode {mode} in slot {slot}, status: {err}")

        ## Set AI sampling rate
        err = dev.AI_setSamplingRate(slot, sampling_rate, timeout)
        print(f"AI_setSamplingRate {sampling_rate} in slot {slot}, status: {err}")

        ## Open AI streaming
        err = dev.AI_openStreaming(slot, timeout)
        print(f"AI_openStreaming in slot {slot}, status: {err}")

        ## Start AI streaming
        err = dev.AI_startStreaming(slot, timeout)
        print(f"AI_startStreaming in slot {slot}, status: {err}")

        ## Wait a while for data acquisition
        time.sleep(1)  ## delay [sec]

        ## Stop AI
        err = dev.AI_stop(slot, timeout)
        print(f"AI_stop in slot {slot}, status: {err}")

        data_len = 1
        while data_len > 0:
            ## Read data acquisition
            ai_2Dlist = dev.AI_readStreaming(slot, read_points, read_delay)
            print(f"number of samples = {len(ai_2Dlist)}")

            ## Update data len
            data_len = len(ai_2Dlist)

        ## Close AI streaming
        err = dev.AI_closeStreaming(slot, timeout)
        print(f"AI_closeStreaming in slot {slot}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()