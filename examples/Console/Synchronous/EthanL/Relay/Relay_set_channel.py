'''
Relay - Relay_set_channel.py with synchronous mode.

This example demonstrates how to write channel from EthanL.

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
    dev = pywpc.EthanL()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        DO_port = 0
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Relay open
        err = dev.Relay_open(port, timeout)
        print(f"Relay_open in port {port}, status: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i % 2 == 0:
                value = [0, 0, 0, 0, 0, 0]
            else:
                value = [1, 1, 1, 1, 1, 1]

            dev.DO_writePort(DO_port, value, timeout)
            print(f'Port: {DO_port}, digital state= {value}')

            ## Wait
            time.sleep(0.5)   ## delay [sec]

        ## Relay close
        err = dev.Relay_close(port, timeout)
        print(f"Relay_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()