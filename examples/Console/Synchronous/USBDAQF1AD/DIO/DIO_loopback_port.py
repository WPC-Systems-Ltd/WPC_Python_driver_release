'''
DIO - DIO_loopback_port.py

This example demonstrates how to write DIO loopback in port from USBDAQF1AD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
Last, close DO and DI in port.

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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port_DO = 0
        port_DI = 1

        ## Open all pins with digital output
        err = dev.DO_openPort(port_DO)
        print("DO_openPort:", err)

        ## Open all pins with digital input
        err = dev.DI_openPort(port_DI)
        print("DI_openPort:", err)

        ## Set pin0, pin1 and pin2 to high, others to low
        err = dev.DO_writePort(port_DO, [0,0,0,1,0,0,0,0])
        print("DO_writePort:", err)

        ## Read all pins state
        state_list = dev.DI_readPort(port_DI)
        print(state_list)

        ## Close all pins with digital output
        err = dev.DO_closePort(port_DO)
        print("DO_closePort:", err)

        ## Close all pins with digital input
        err = dev.DI_closePort(port_DI)
        print("DI_closePort:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()