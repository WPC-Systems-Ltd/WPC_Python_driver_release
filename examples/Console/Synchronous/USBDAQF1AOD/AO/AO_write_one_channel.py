'''
AO - AO_write_one_channel.py with synchronous mode.

This example demonstrates the process of writing AO signal of USBDAQF1AOD.
To begin with, it demonstrates the steps to open the AO port.
Next, it outlines the procedure for writing digital signals with channel to the AO pins.
Finally, it concludes by explaining how to close the AO port.

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
        print(f"AO_open in port {port}: {err}")

        ## Set AO port and write data 1.5(V) in channel 0
        err = dev.AO_writeOneChannel(port, 0, 1.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch0 in port {port}: {err}")

        ## Set AO port and write data 2.5(V) in channel 1
        err = dev.AO_writeOneChannel(port, 1, 2.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch1 in port {port}: {err}")

        ## Set AO port and write data 3.5(V) in channel 2
        err = dev.AO_writeOneChannel(port, 2, 3.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch2 in port {port}: {err}")

        ## Set AO port and write data 4.5(V) in channel 3
        err = dev.AO_writeOneChannel(port, 3, 4.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch3 in port {port}: {err}")

        ## Close AO
        err = dev.AO_close(port)
        print(f"AO_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()