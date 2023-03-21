'''
AO - AO_write_all_channels.py with synchronous mode.

This example demonstrates how to write AO in all channels from USBDAQF1AOD.

First, it shows how to open AO in port.
Second, write all digital signals
Last, close AO in port.

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
    dev = pywpc.USBDAQF1AOD()

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
        port = 0 ## Depend on your device
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AO
        err = dev.AO_open(port, timeout=timeout)
        print(f"AO_open in port{port}: {err}")

        ## Set AO port and write data simultaneously
        err = dev.AO_writeAllChannels(port, [0,1,2,3,4,5,4,3], timeout=timeout)
        print(f"AO_writeAllChannels in port{port}: {err}")

        ## Close AO
        err = dev.AO_close(port, timeout=timeout)
        print(f"AO_close in port{port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()