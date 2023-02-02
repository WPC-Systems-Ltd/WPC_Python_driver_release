'''
System_USB - get_USB_info.py

This example demonstrates how to get hardware information from USBDAQF1D.

First, get hardware information such as firmware model & version.
Last, get serial number and RTC.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to device
    try:
        dev.connect("21JA1200")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform DAQ basic information
    try:
        ## Parameters setting
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get serial number & RTC Time
        print(f'Serial number = ' + dev.Sys_getSerialNumber(timeout))
        print(f'RTC data time = ' + dev.Sys_getRTC(timeout))

    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()