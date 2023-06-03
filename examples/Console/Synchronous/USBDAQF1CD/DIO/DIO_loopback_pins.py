'''
DIO - DIO_loopback_pins.py with synchronous mode.

This example demonstrates the process of DIO loopback using pins from USBDAQF1CD.
It involves using DO pins to send signals and DI pins to receive signals on a single device, commonly known as "loopback".

To begin with, it illustrates the steps required to open the DO and DI pins.
Next, it performs the operation of writing to a DO pin and reading from a DI pin.
Lastly, it concludes by closing the DO and DI pins.

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
    dev = pywpc.USBDAQF1CD()

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
        timeout = 3  ## second
        DO_pins = [0, 1, 2, 3]
        DI_pins = [4, 5, 6, 7]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pins with digital output
        err = dev.DO_openPins(port, DO_pins, timeout=timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Write pins to high or low
        err = dev.DO_writePins(port, DO_pins, [1, 1, 0, 0], timeout=timeout)
        print(f"DO_writePins in {[port]}: {err}")

        ## Open pins with digital iutput
        err = dev.DI_openPins(port, DI_pins, timeout=timeout)
        print(f"DI_openPins in port {port}: {err}")

        ## Read pins state
        state_list = dev.DI_readPins(port, DI_pins, timeout=timeout)
        print(f"state_list in port {port}: {state_list}")

        ## Close pins with digital output
        err = dev.DO_closePins(port, DO_pins, timeout=timeout)
        print(f"DO_closePins in port {port}: {err}")

        ## Close pins with digital input
        err = dev.DI_closePins(port, DI_pins, timeout=timeout)
        print(f"DI_closePins in port {port}: {err}")
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()