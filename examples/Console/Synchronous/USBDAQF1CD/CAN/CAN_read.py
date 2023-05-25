'''
CAN - CAN_read.py with synchronous mode.

This example demonstrates how to read data from another device with CAN interface from USBDAQF1CD.

First, it shows how to open CAN port and configure CAN parameters.
Second, read bytes from another device.
Last, stop and close CAN port.

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
        delay = 0.005 ## second
        timeout = 3  ## second

        ## Get Firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open CAN
        err = dev.CAN_open(port, timeout=timeout)
        print(f"CAN_open in port {port}: {err}")

        ## Set CAN port and set speed to 0
        err = dev.CAN_setSpeed(port, speed, timeout=timeout)
        print(f"CAN_setSpeed in port {port}: {err}")

        ## Set CAN port and start CAN
        err = dev.CAN_start(port, timeout=timeout)
        print(f"CAN_start in port {port}: {err}")

        ## Read 5 frames for 1000 times
        for i in range(1000):
            frame_list = dev.CAN_read(port, 5, delay=delay)
            if len(frame_list) > 0 :
                for frame in frame_list:
                    print(frame)
            else:
                ## Wait for 0.01 seconds
                time.sleep(0.01) ## delay [s]

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