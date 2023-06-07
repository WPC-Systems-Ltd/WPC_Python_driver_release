'''
DIO - DO_write_pins.py with synchronous mode.

This example illustrates the process of writing a high or low signal to a DO pin from USBDAQF1AOD.

To begin with, it demonstrates the steps required to open the DO pin.
Next, voltage output is written to the DO pin.
Lastly, it concludes by closing the DO pin.

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
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        pin_index = [0, 1, 2, 3]
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pins with digital output
        err = dev.DO_openPins(port, pin_index, timeout=timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Write pins to high or low
        err = dev.DO_writePins(port, pin_index, [1, 1, 0, 0], timeout=timeout)
        print(f"DO_writePins in port {port}: {err}")

        ## Wait for 1 seconds to see led status
        time.sleep(1) ## delay [s]

        ## Close pins with digital output
        err = dev.DO_closePins(port, pin_index, timeout=timeout)
        print(f"DO_closePins in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()