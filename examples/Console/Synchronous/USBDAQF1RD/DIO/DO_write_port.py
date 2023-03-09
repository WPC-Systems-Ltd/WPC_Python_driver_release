'''
DIO - DO_write_port.py with synchronous mode.

This example demonstrates how to write DO in port from USBDAQF1RD.

First, it shows how to open DO in port.
Second, write DO pins in two different types (hex or list) but it should be consistency.
Last, close DO in port.

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
    dev = pywpc.USBDAQF1RD()

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

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open all pins and set it to digital output
        err = dev.DO_openPort(port, timeout)
        print(f"DO_openPort in port{port}: {err}")

        ## Set pin0, pin3 and pin4 to high, others to low
        err = dev.DO_writePort(port, [0,0,0,1,1,0,0,1], timeout)
        print(f"DO_writePort in port{port}: {err}")

        ## Wait for 1 seconds to see led status
        time.sleep(1) ## delay [s]

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex)
        err = dev.DO_writePort(port, 0xC0, timeout)
        print(f"DO_writePort in port{port}: {err}")

        ## Close all pins with digital output
        err = dev.DO_closePort(port, timeout)
        print(f"DO_closePort in port{port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()