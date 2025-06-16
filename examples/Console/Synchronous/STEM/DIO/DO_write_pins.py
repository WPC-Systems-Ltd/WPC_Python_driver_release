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
        port = 0  ## Depend on your device
        pin_index = [0, 1, 2, 3]
        DO_value = [1, 0, 1, 0]
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open pins with digital output
        err = dev.DO_openPins(port, pin_index, timeout)
        print(f"DO_openPins in port {port}, status: {err}")

        ## Write pins to high or low
        err = dev.DO_writePins(port, pin_index, DO_value, timeout)
        print(f"DO_writePins in port {port}, status: {err}")

        ## Wait for seconds to see led status
        time.sleep(3)  ## delay [sec]

        ## Close pins with digital output
        err = dev.DO_closePins(port, pin_index, timeout)
        print(f"DO_closePins in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()