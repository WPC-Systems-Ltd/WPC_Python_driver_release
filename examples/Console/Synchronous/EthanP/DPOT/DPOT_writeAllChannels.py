'''
DPOT - DPOT_writeAllChannels.py with asynchronous mode.

This example demonstrates how to write digital potentiometer resistance to all channel from EthanP.
-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanP()

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
        resistance_ratio = [0.5, 0.2, 0.8, 0.7]
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open DPOT
        err = dev.DPOT_open(port, timeout)
        print(f"DPOT_open in port {port}, status: {err}")

        ## Write all channels
        err = dev.DPOT_writeAllChannel(port, resistance_ratio, timeout)
        print(f"DPOT_writeAllChannel in port {port}, status: {err}")

        ## Close DPOT
        err = dev.DPOT_close(port, timeout)
        print(f"DPOT_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()