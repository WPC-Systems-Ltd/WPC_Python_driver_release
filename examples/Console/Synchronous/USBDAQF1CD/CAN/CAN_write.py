'''
CAN - CAN_write.py with synchronous mode.

This example demonstrates how to write data to another device with CAN interface from USBDAQF1CD.

First, it shows how to open CAN port and configure CAN parameters.
Second, write bytes to another device.
Last, stop and close CAN port.

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
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

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
        speed = 0 ## 0 = 125 KHz, 1 = 250 kHz, 2 = 500 kHz, 3 = 1 MHz
        timeout = 3  ## second

        ## Get Firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open CAN
        err = dev.CAN_open(port, timeout=timeout)
        print(f"CAN_open in port {port}: {err}")

        ## Set CAN port and set speed to 0
        err =  dev.CAN_setSpeed(port, speed, timeout=timeout)
        print(f"CAN_setSpeed in port {port}: {err}")

        ## Set CAN port and start CAN
        err = dev.CAN_start(port, timeout=timeout)
        print(f"CAN_start in port {port}: {err}")

        ## CAN_length: True: Extended, False: Standard
        ## CAN_type:   True: Remote, False: Data

        ## ID: 10, data with 8 bytes, Standard & Data
        err = dev.CAN_write(port, 10, [33, 22, 11, 88, 77, 55, 66, 22], False, False, timeout=timeout)
        print(f"CAN_write in port {port}: {err}")

        ## Wait for 1 sec
        time.sleep(1) ## delay [s]

        ## ID: 20, data less than 8 bytes, Standard & Data
        err = dev.CAN_write(port, 20, [1, 2, 3], False, False, timeout=timeout)
        print(f"CAN_write in port {port}: {err}")

        ## Wait for 1 sec
        time.sleep(1) ## delay [s]

        ## Set CAN port and stop CAN
        err = dev.CAN_stop(port, timeout=timeout)
        print(f"CAN_stop in port {port}: {err}")

        ## Close CAN
        err = dev.CAN_close(port, timeout=timeout)
        print(f"CAN_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()