'''
AI - AI_on_demand_in_loop.py with synchronous mode.

This example demonstrates the process of obtaining AI data in on demand mode.
Additionally, it utilizes a loop to retrieve AI data with 5 times from USBDAQF1AD.

To begin with, it demonstrates the steps to open the AI port and configure the AI parameters.
Next, it outlines the procedure for reading the AI on demand data.
Finally, it concludes by explaining how to close the AI port.

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

def loop_func(handle, port, delay=0.05, exit_loop_time=3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## data acquisition
        data = handle.AI_readOnDemand(port)
        if len(data) > 0:
            print(f"data in port {port}: {data}")

        ## Wait
        time.sleep(delay) ## delay [s]
        time_cal += delay

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

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
        mode = 0
        timeout = 3  ## second
        chip_select = [0, 1]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Open port
        err = dev.AI_open(port, timeout=timeout)
        print(f"AI_open in port {port}: {err}")
        
        ## Set AI acquisition mode to on demand mode (0)
        err = dev.AI_setMode(port, mode, timeout=timeout)
        print(f"AI_setMode {mode} in port {port}: {err}")

        ## Read AI data with 5 times
        print(f"data in port {port}: ")
        for i in range(5):
            ## data acquisition
            data = dev.AI_readOnDemand(port)
            print(f"{data}")

        ## Close port
        err = dev.AI_close(port, timeout=timeout)
        print(f"AI_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()