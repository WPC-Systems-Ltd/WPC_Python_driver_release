'''
AI - AI_on_demand_once.py with synchronous mode.

This example demonstrates the process of obtaining AI data in on demand mode.
Additionally, it retrieve AI data from WifiDAQF4A.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the AI on demand data.
Finally, it concludes by explaining how to close the AI.

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
    dev = pywpc.WifiDAQF4A()

    ## Connect to device
    try:
        dev.connect("192.168.5.38")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        mode = 0
        timeout = 3  ## [sec]
        
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open AI
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port {port}, status: {err}")
        
        ## Set AI acquisition mode to on demand mode (0)
        err = dev.AI_setMode(port, mode, timeout)
        print(f"AI_setMode {mode} in port {port}, status: {err}")

        ## Read AI
        ai_list = dev.AI_readOnDemand(port, timeout)
        print(f"Data in port {port}: {ai_list}")

        ## Close AI
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()