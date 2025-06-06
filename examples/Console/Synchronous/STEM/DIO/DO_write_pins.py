'''
DIO - DO_write_pins.py with synchronous mode.

This example illustrates the process of writing a high or low signal to a DO pin from STEM.

To begin with, it demonstrates the steps required to open the DO pin.
Next, voltage output is written to the DO pin.
Lastly, it concludes by closing the DO pin.

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
        slot = 1 ## Connect DIO module to slot
        DO_port = 0
        pin_index = [0, 1, 2, 3]
        DO_value = [1, 0, 1, 0]
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
            print(f"Sys_setDIOMode in slot {slot}, status: {err}")

        ## Get slot mode
        slot_mode = dev.Sys_getMode(slot, timeout)
        print("Slot mode:", slot_mode)

        ## Get DIO start up information
        info = dev.DIO_loadStartup(DO_port, timeout)
        print("Enable:   ", info[0])
        print("Direction:", info[1])
        print("State:    ", info[2])

        ## Write pins to high or low
        err = dev.DO_writePins(DO_port, pin_index, DO_value, timeout)
        print(f"DO_writePins in port {DO_port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()