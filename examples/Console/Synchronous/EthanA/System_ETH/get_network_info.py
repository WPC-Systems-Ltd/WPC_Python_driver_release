'''
System_ETH - get_network_info.py

This example demonstrates how to get hardware & network information from EthanA.

First, get hardware information such as firmware model & version.
Last, get network information such as IP & submask & MAC.

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
    dev = pywpc.EthanA()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform DAQ basic information
    try:
        ## Parameters setting
        timeout = 3  ## second
        
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get IP & submask
        ip_addr, submask = dev.Net_getIPAddrAndSubmask(timeout)
        print(f'IP = ' + ip_addr)
        print(f'Submask = '+ submask)
        
        ## Get MAC
        MAC= dev.Net_getMACAddr(timeout)
        print(f'MAC = ' + MAC)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()