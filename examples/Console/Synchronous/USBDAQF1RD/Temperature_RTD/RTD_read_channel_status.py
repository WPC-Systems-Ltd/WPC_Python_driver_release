'''
Temperature_RTD - RTD_read_channel_status.py with synchronous mode.

This example demonstrates how to get status in two channels from USBDAQF1RD.

First, it shows how to open thermal port
Second, get status from channel 0 and channel 1
Last, close thermal port.

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
        port = 1 ## Depend on your device
        ch0 = 0
        ch1 = 1
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open RTD
        err = dev.Thermal_open(port, timeout)
        print(f"Thermal_open in port {port}: {err}")

        ## Set RTD port and get status in channel 0
        status = dev.Thermal_getStatus(port, ch0, timeout)
        print(f"Thermal_getStatus in channel {ch0} status: {status}")

        ## Set RTD port and get status in channel 1
        status = dev.Thermal_getStatus(port, ch1, timeout)
        print(f"Thermal_getStatus in channel {ch1} status: {status}")

        ## Close RTD
        err = dev.Thermal_close(port, timeout)
        print(f"Thermal_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()