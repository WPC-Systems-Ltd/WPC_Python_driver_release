'''
Counter - Counter_read.py with synchronous mode.

This example demonstrates how to read counter with USBDAQF1TD.

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
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

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
        channel = 1 ## Depend on your device
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open counter
        err = dev.Counter_open(channel, timeout=timeout)
        print(f"Counter_open in channel {channel}: {err}")

        ## Start counter
        err = dev.Counter_start(channel, timeout=timeout)
        print(f"Counter_start in channel {channel}: {err}")

        ## Read counter
        for i in range(10):
            counter = dev.Counter_read(channel, timeout=timeout)
            print(f"Read counter in channel {channel}: {counter}")

        ## Stop counter
        err = dev.Counter_stop(channel, timeout=timeout)
        print(f"Counter_stop in channel {channel}: {err}")

        ## Close counter
        err = dev.Counter_close(channel, timeout=timeout)
        print(f"Counter_close in channel {channel}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()