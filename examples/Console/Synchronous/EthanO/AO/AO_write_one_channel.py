'''
AO - AO_write_one_channel.py

This example demonstrates how to write AO in specific channels from EthanO.

First, it shows how to open AO in port.
Second, write digital signals in specific channels.
Last, close AO in port.

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
    dev = pywpc.EthanO()

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

        ## Open AO
        err = dev.AO_open(port)
        print("AO_open:", err)

        ## Set AO port and write data 1.5(V) in channel 4
        err = dev.AO_writeOneChannel(port, 4, 1.5)
        print("AO_writeOneChannel:", err)

        ## Set AO port and write data 2.5(V) in channel 5
        err = dev.AO_writeOneChannel(port, 5, 2.5)
        print("AO_writeOneChannel:", err)

        ## Set AO port and write data 3.5(V) in channel 6
        err = dev.AO_writeOneChannel(port, 6, 3.5)
        print("AO_writeOneChannel:", err)

        ## Set AO port and write data 4.5(V) in channel 7
        err = dev.AO_writeOneChannel(port, 7, 4.5)
        print("AO_writeOneChannel:", err)

        ## Close AO
        err = dev.AO_close(port)
        print("AO_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()