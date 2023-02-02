'''
AI - AI_on_demand_in_loop.py

This example demonstrates how to get AI data in on demand mode.
Also, it uses loop to get AI data with 3 seconds timeout with 8 channels USBDAQF1AD.

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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Parameters setting
        port = 0
        mode = 0
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Open port
        err = dev.AI_open(port, timeout)
        print("AI_open:", err)

        ## Set AI port and acquisition mode to on demand mode (0)
        err = dev.AI_setMode(port, mode, timeout)
        print("AI_setMode:", err)

        ## Set AI port and start thread
        delay = 1
        exit_loop_time = 3
        
        loop_func(dev, port, delay, exit_loop_time)

        ## Close port
        err = dev.AI_close(port, timeout)
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