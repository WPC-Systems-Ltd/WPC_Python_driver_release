'''
AO - AO_write_all_channels.py with synchronous mode.

This example demonstrates the process of writing AO signal of EthanO.
To begin with, it demonstrates the steps to open AO.
Next, it outlines the procedure for writing digital signals simultaneously to the AO pins.
Finally, it concludes by explaining how to close AO.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanO()

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
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AO
        err = dev.AO_open(port, timeout)
        print(f"AO_open in port {port}, status: {err}")

        ## Write AO value simultaneously
        err = dev.AO_writeAllChannels(port, ao_value_list, timeout)
        print(f"In port {port} the AO value is {ao_value_list}, status: {err}")

        ## Close AO
        err = dev.AO_close(port)
        print(f"AO_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()