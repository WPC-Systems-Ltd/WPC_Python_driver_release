'''
AHRS - AHRS_getAcceleration.py with synchronous mode.

This example demonstrates the process of getting AHRS three axis acceleration data from WifiDAQE3AH.

To begin with, it demonstrates the steps to open the AHRS and configure the AHRS parameters.
Next, it outlines the procedure for the AHRS acceleration data.
Finally, it concludes by explaining how to close the AHRS.

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
    dev = pywpc.WifiDAQE3AH()

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
        port = 0 ## Depend on your device
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AHRS and update rate is 333 HZ
        err = dev.AHRS_open(port, timeout)
        print(f"AHRS_open in port {port}, status: {err}")

        ## Start AHRS
        err = dev.AHRS_start(port, timeout)
        print(f"AHRS_start in port {port}, status: {err}")

        ## Get three axis acceleration
        while True:
            data = dev.AHRS_getAcceleration(port, timeout)
            print(data)
    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop AHRS
        err = dev.AHRS_stop(port, timeout)
        print(f"AHRS_stop in port {port}, status: {err}")

        ## Close AHRS
        err = dev.AHRS_close(port, timeout)
        print(f"AHRS_close in port {port}, status: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

    return
if __name__ == '__main__':
    main()