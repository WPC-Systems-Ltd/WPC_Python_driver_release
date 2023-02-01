'''
Temperature_RTD - RTD_read_channel_data.py

This example demonstrates how to read RTD data in two channels from USBDAQF1RD.

First, it shows how to open thermal port
Second, read channel 0 and channel 1 RTD data
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
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("21JA1385")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        channel_0 = 0
        channel_1 = 1

        ## Open RTD
        err = dev.Thermal_open(port)
        print("Thermal_open:", err)

        ## Sleep
        time.sleep(0.1) ## delay(second)

        ## Set RTD port and read RTD in channel 0
        data0 =  dev.Thermal_readSensor(port, channel_0)
        print("Read channel 0 data:", data0, "°C")

        ## Set RTD port and read RTD in channel 1
        data1 = dev.Thermal_readSensor(port, channel_1)
        print("Read channel 1 data:", data1, "°C")

        ## Close RTD
        err = dev.Thermal_close(port)
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