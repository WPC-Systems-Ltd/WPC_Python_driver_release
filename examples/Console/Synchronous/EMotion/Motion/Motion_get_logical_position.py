'''
Motion - Motion_get_logical_position.py with synchronous mode.

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
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        axis = 0
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port {port}, status: {err}")

        for i in range(100):
            err = dev.Motion_setLogicalPosi(port, axis, i, timeout)
            if err != 0:
                print(f"Motion_setLogicalPosi in axis{axis}, status: {err}")
            posi = dev.Motion_getLogicalPosi(port, axis, timeout)
            print(f"Motion_getLogicalPosi in axis{axis}: {posi}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()