'''
System_Wifi - get_network_info.py with synchronous mode.

This example demonstrates how to get hardware & network information from WifiDAQF4A.

First, get hardware information such as firmware model & version.
Last, get network information such as IP & submask & MAC.

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
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Get IP & submask
        ip_addr, submask = dev.Net_getIPAddrAndSubmask(timeout)
        print(f"IP: {ip_addr}")
        print(f"Submask: {submask}")

        ## Get MAC
        mac = dev.Net_getMACAddr(timeout)
        print(f"MAC: {mac}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect network device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()