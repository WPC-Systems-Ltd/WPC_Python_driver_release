'''
System_USB - hello_world.py with synchronous mode.

This example code is in the public domain from USBDAQF1DSNK.

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
    dev = pywpc.USBDAQF1DSNK()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        timeout = 3  ## [sec]

        for i in range(10, 0, -1):
            print(f"Restarting in {i} seconds...")
            time.sleep(1)  ## delay [sec]

        print("Restarting now")
        dev.Sys_reboot(timeout)
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect USB device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()