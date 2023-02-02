'''
System_Wifi - get_Wifi_DAQ_status.py

This example demonstrates how to get basic information such as RSSI & battery & thermo from WifiDAQE3A.

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
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform to Get RSSI, Battery and Thermo
    try:
        ## Parameters setting
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Firmware model:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get RSSI, battery and thermo
        data1 = dev.Wifi_readRSSI(timeout)
        data2 = dev.Wifi_readBattery(timeout)
        data3 = dev.Wifi_readThermo(timeout)

        print("RSSI:" + str(data1) + " dBm")
        print("Battery:"+ str(data2) + " mV")
        print("Thermo:"+ str(data3) + " °C")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return
if __name__ == '__main__':
    main()