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

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc


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
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        timeout = 3  ## [sec]

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

        ## Open AO
        err = dev.AO_open(slot, timeout)
        print(f"AO_open in slot {slot}, status: {err}")

        ## Write AO vaule in channel 0
        err = dev.AO_writeOneChannel(slot, 0, ao_value_list[0], timeout)
        print(f"In slot {slot} channel 0, the AO value is {ao_value_list[0]}, status: {err}")

        ## Write AO vaule in channel 1
        err = dev.AO_writeOneChannel(slot, 1, ao_value_list[1], timeout)
        print(f"In slot {slot} channel 1, the AO value is {ao_value_list[1]}, status: {err}")

        ## Write AO vaule in channel 2
        err = dev.AO_writeOneChannel(slot, 2, ao_value_list[2], timeout)
        print(f"In slot {slot} channel 2, the AO value is {ao_value_list[2]}, status: {err}")

        ## Write AO vaule in channel 3
        err = dev.AO_writeOneChannel(slot, 3, ao_value_list[3], timeout)
        print(f"In slot {slot} channel 3, the AO value is {ao_value_list[3]}, status: {err}")

        ## Close AO
        err = dev.AO_close(slot)
        print(f"AO_close in slot {slot}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()