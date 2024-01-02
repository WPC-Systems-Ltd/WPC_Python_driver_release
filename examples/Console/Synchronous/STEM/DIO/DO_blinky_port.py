'''
DIO - DO_blinky_port.py with synchronous mode.

This example illustrates the process of writing a high or low signal to a DO port from STEM.

To begin with, it demonstrates the steps required to open the DO port.
Next, in each loop, a different voltage output is applied, resulting in a blinking effect.
Lastly, it concludes by closing the DO port.

If your product is "STEM", please invoke the function `Sys_setDIOMode`.

The DIO ports 0 to 1 are assigned to slot 1, while ports 2 to 3 are assigned to slot 2.
---------------------------
|  Slot 1    port 1 & 0   |
|  Slot 2    port 3 & 2   |
|  Slot 3    port 5 & 4   |
|  Slot 4    port 7 & 6   |
---------------------------

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
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
        slot = 1 ## Connect DIO module to slot
        DO_port = 1
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout)
        print("Slot mode:", slot_mode)

        ## If the slot mode is not set to "DIO", set the slot mode to "DIO"
        if slot_mode != "DIO":
            err = dev.Sys_setDIOMode(slot, timeout)
            print(f"Sys_setDIOMode in slot {slot}: {err}")

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout)
        print("Slot mode:", slot_mode)

        ## Get DIO start up information
        info = dev.DIO_loadStartup(DO_port, timeout)
        print("Enable:   ", info[0])
        print("Direction:", info[1])
        print("State:    ", info[2])

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            state = dev.DO_togglePort(DO_port, timeout)
            print(state)

            ## Wait for 0.5 second to see led status
            time.sleep(0.5) ## delay [s]
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()