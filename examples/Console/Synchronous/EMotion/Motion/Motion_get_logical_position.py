'''
Motion - Motion_get_logical_position.py
 
For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
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
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        axis = 0
        stop_decel = 0 
        ## Motion open
        err = dev.Motion_open(port)
        print("Motion_open:", err)

        for i in range(100):
            err = dev.Motion_setLogicalPosi(port, axis, i)
            if err != 0:
                print("Motion_setLogicalPosi ", err)
            posi = dev.Motion_getLogicalPosi(port, axis)
            print("Motion_getLogicalPosi ", posi)
            
        ## Motion close
        err = dev.Motion_close(port)
        print("Motion_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return
if __name__ == '__main__':
    main()