'''
Temperature_TC - TC_read_channel_status.py with synchronous mode.

This example demonstrates how to get status from USBDAQF1TD.

First, it shows how to open thermal port
Second, get status from channel 0 and channel 1
Last, close thermal port.

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
    dev = pywpc.USBDAQF1TD()

    ## Connect to device
    try:
        dev.connect("21JA1239")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Parameters setting
        port = 1
        channel_0 = 0
        channel_1 = 1
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])
 
        ## Open thermo
        err = dev.Thermal_open(port, timeout)
        print("Thermal_open:", err)

        ## Set thermo port and get status in channel 0
        status = dev.Thermal_getStatus(port, channel_0, timeout)
        print("Thermal_getStatus in chaannel 0:", status)

        ## Set thermo port and get status in channel 1
        status = dev.Thermal_getStatus(port, channel_1, timeout)
        print("Thermal_getStatus in chaannel 1:", status)

        ## Close thermo
        err = dev.Thermal_close(port, timeout)
        print("Thermal_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
    
if __name__ == '__main__':
    main()