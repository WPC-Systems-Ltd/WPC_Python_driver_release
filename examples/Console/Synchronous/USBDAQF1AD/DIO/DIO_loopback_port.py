'''
DIO - DIO_loopback_port.py with synchronous mode.

This example demonstrates how to write DIO loopback in port from USBDAQF1AD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
Last, close DO and DI in port.

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
    dev = pywpc.USBDAQF1AD()

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
        port_DO = 0
        port_DI = 1
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open all pins with digital output
        err = dev.DO_openPort(port_DO, timeout)
        print(f"DO_openPort in port {port_DO}: {err}")

        ## Open all pins with digital input
        err = dev.DI_openPort(port_DI, timeout)
        print(f"DI_openPort in port {port_DI}: {err}")

        ## Set pin0, pin1 and pin2 to high, others to low
        err = dev.DO_writePort(port_DO, [0,0,0,1,0,0,0,0], timeout)
        print(f"DO_writePort in port {port_DO}: {err}")

        ## Read all pins state
        state_list = dev.DI_readPort(port_DI, timeout)
        print(f"state_list in port {port_DI}: {state_list}")

        ## Close all pins with digital output
        err = dev.DO_closePort(port_DO, timeout)
        print(f"DO_closePort in port {port_DO}: {err}")

        ## Close all pins with digital input
        err = dev.DI_closePort(port_DI, timeout)
        print(f"DI_closePort in port {port_DI}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()