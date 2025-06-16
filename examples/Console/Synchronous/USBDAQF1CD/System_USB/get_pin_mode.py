'''
System_USB - get_pin_mode.py with synchronous mode.

This example demonstrates how to get pin mode from USBDAQF1CD.

First, get idle pin mode and show how to open DO and DI in pins.
Second, get idle pin mode and set port idle mode. Again, get pin mode.
Last, close DO and DI in port.

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
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = None  ## Depend on your device
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Firmware model:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get pinmode from port 0 to port 3
        for i in range(4):
            ## Get pin mode
            pin_mode = dev.Sys_getPinModeInPort(i, timeout)
            print("pin_mode", pin_mode)
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect USB device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()