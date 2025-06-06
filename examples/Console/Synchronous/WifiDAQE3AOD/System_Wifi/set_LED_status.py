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

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AOD()

    ## Connect to device
    try:
        dev.connect("192.168.5.38") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        timeout = 3 ## second
        value = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        for i in range(3):
            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set green LED status
            err = dev.Wifi_setGreenLED(value, timeout)
            print(f"Wifi_setGreenLED, status: {err}")
            time.sleep(1) ## delay [s]

            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set blue LED status
            err = dev.Wifi_setBlueLED(value, timeout)
            print(f"Wifi_setBluLeED, status: {err}")
            time.sleep(1) ## delay [s]

            ## Reset LED status
            err = dev.Wifi_resetLED(timeout)
            print(f"Wifi_resetLED, status: {err}")

            ## Set red LED status
            err = dev.Wifi_setRedLED(value, timeout)
            print(f"Wifi_setRedLED, status: {err}")
            time.sleep(1) ## delay [s]

            print("")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()