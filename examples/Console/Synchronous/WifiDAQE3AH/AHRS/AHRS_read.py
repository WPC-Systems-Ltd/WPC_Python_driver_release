'''
AHRS - AHRS_read.py with synchronous mode.

This example demonstrates the process of obtaining AHRS three axis estimation data.

To begin with, it demonstrates the steps to open the AHRS and configure the AHRS parameters.
Next, it outlines the procedure for reading the streaming AHRS data.
Finally, it concludes by explaining how to close the AHRS.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
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
        sampling_period = 0.003
        mode = 0 ## 0: Orientation, 1: Acceleration, 2: Orientation + Acceleration
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = dev.AHRS_open(port, timeout)
        print(f"AHRS_open in port {port}: {err}")

        ## Set period
        err = dev.AHRS_setSamplingPeriod(port, sampling_period, timeout)
        print(f"AHRS_setSamplingPeriod in port {port}: {err}")

        ## Start AHRS
        err = dev.AHRS_start(port, timeout)
        print(f"AHRS_start in port {port}: {err}")

        ## Read AHRS data
        while True:
            ahrs_list = dev.AHRS_getEstimate(port, mode, timeout)
            print(ahrs_list)

    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop AHRS
        err = dev.AHRS_stop(port, timeout)
        print(f"AHRS_stop in port {port}: {err}")

        ## Close AHRS
        err = dev.AHRS_close(port, timeout)
        print(f"AHRS_close in port {port}: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

    return
if __name__ == '__main__':
    main()