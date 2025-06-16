'''
System_Wifi - set_LED_status.py with synchronous mode.

This example demonstrates how to set LED status from WifiDAQE3AOD.

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
    dev = pywpc.WifiDAQE3AOD()

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
        timeout = 3  ## [sec]
        value = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        for i in range(3):
            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set green LED status
            err = dev.Wifi_setGreenLED(value, timeout)
            print(f"Wifi_setGreenLED, status: {err}")
            time.sleep(1)  ## delay [sec]

            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set blue LED status
            err = dev.Wifi_setBlueLED(value, timeout)
            print(f"Wifi_setBluLeED, status: {err}")
            time.sleep(1)  ## delay [sec]

            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set red LED status
            err = dev.Wifi_setRedLED(value, timeout)
            print(f"Wifi_setRedLED, status: {err}")
            time.sleep(1)  ## delay [sec]

            print("")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect network device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()