'''
AIO - AIO_all_channels_loopback.py with synchronous mode.

This example demonstrates the process of AIO loopback across all channels of STEM.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO.
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

If your product is "STEM", please invoke the function `Sys_setAIOMode` and `AI_enableCS`.
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

## Python
import time

## WPC

from wpcsys import pywpc


def main():
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
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        timeout = 3 ## second
        chip_select = [0]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

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

        ## Open AO
        err = dev.AO_open(slot, timeout)
        print(f"AO_open in slot {slot}, status: {err}")

        ## Read data acquisition
        ai_list = dev.AI_readOnDemand(slot, timeout)
        print(f"AI data in slot {slot}: {ai_list}")

        ## Write AO value simultaneously
        err = dev.AO_writeAllChannels(slot, ao_value_list, timeout)
        print(f"In slot {slot} the AO value is {ao_value_list}, status: {err}")

        ## Read data acquisition
        ai_list = dev.AI_readOnDemand(slot, timeout)
        print(f"AI data in slot {slot}: {ai_list}")

        ## Close AI
        err = dev.AI_close(slot, timeout)
        print(f"AI_close in slot {slot}, status: {err}")

        ## Close AO
        err = dev.AO_close(slot, timeout)
        print(f"AO_close in slot {slot}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()