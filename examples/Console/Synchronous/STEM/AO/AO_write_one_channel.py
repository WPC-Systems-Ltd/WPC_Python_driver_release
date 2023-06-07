'''
AO - AO_write_one_channel.py with synchronous mode.

This example demonstrates the process of writing AO signal of STEM.
To begin with, it demonstrates the steps to open AO.
Next, it outlines the procedure for writing digital signals with channel to the AO pins.
Finally, it concludes by explaining how to close AO.

If your product is "STEM", please invoke the function `Sys_setAIOMode`.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout=timeout)
        print("Slot mode:", slot_mode)

        ## If the slot mode is not set to "AIO", set the slot mode to "AIO"
        if slot_mode != "AIO":
            err = dev.Sys_setAIOMode(slot, timeout=timeout)
            print(f"Sys_setAIOMode in slot {slot}: {err}")

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout=timeout)
        print("Slot mode:", slot_mode)
        
        ## Open AO
        err = dev.AO_open(slot, timeout=timeout)
        print(f"AO_open in slot {slot}: {err}")

        ## Write AO 1.5(V) in channel 0
        err = dev.AO_writeOneChannel(slot, 0, 1.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch0 in slot {slot}: {err}")

        ## Write AO 2.5(V) in channel 1
        err = dev.AO_writeOneChannel(slot, 1, 2.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch1 in slot {slot}: {err}")

        ## Write AO 3.5(V) in channel 2
        err = dev.AO_writeOneChannel(slot, 2, 3.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch2 in slot {slot}: {err}")

        ## Write AO 4.5(V) in channel 3
        err = dev.AO_writeOneChannel(slot, 3, 4.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch3 in slot {slot}: {err}")

        ## Close AO
        err = dev.AO_close(slot)
        print(f"AO_close in slot {slot}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()