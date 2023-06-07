'''
System_Wifi - get_Wifi_DAQ_status.py with synchronous mode.

This example demonstrates how to get basic information such as RSSI & battery & thermo from WifiDAQF4A.

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
    dev = pywpc.WifiDAQF4A()

    ## Connect to device    ## Connect to device
    try:
        dev.connect("192.168.5.35") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = None ## Depend on your device
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Firmware model:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get RSSI, battery and thermo
        rssi = dev.Wifi_readRSSI(timeout=timeout)
        battery = dev.Wifi_readBattery(timeout=timeout)
        thermo = dev.Wifi_readThermo(timeout=timeout)

        print(f"RSSI: {rssi} dBm")
        print(f"Battery: {battery} mV")
        print(f"Thermo: {thermo} °C")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()