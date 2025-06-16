'''
System_Wifi - set_and_get_RTC.py with synchronous mode.

This example demonstrates how to set and get RTC from WifiDAQE3AH.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc

## Python
import time


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AH()

    ## Connect to device
    try:
        dev.connect("192.168.5.38")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        delay = 1  ## [sec]
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Set RTC
        err = dev.Sys_setRTC(2023, 5, 8, 15, 8, 7, timeout)
        print(f"Set RTC to 2023-05-08, 15:08:07 , status: {err}")

        for i in range(10):
            ## Get RTC
            print(f"Get RTC: {dev.Sys_getRTC()}")

            time.sleep(delay)  ## delay [sec]

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect network device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()