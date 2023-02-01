'''
AI - AI_on_demand_in_loop.py

This example demonstrates how to get AI data in on demand mode.
Also, it uses async loop to get AI data with 3 seconds timeout with 8 channels EthanA.

First, it shows how to open AI port and configure AI parameters.
Second, read AI ondemand data.
Last, close AI port.

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

def loop_func(handle, port, delay, exit_loop_time = 3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## data acquisition
        data = handle.AI_readOnDemand(port)
        if len(data) > 0:
            ## Print data
            print("data :" + str(data))
        time.sleep(delay)
        time_cal += delay

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanA()

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
        mode = 0

        ## Open port
        err = dev.AI_open(port)
        print("AI_open:", err)

        ## Set AI port and acquisition mode to on demand mode (0)
        err = dev.AI_setMode(port, mode)
        print("AI_setMode:", err)

        ## Set AI port and start async thread
        loop_func(dev, port, 1, 3)

        ## Close port
        err = dev.AI_close(port)
        print("AI_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()