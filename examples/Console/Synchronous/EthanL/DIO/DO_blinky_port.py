'''
DIO - DO_blinky_port.py

This example demonstrates how to write DO high or low in port from EthanL.

First, it shows how to open DO in port.
Second, each loop has different voltage output so it will look like blinking.
Last, close DO in port.

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
    dev = pywpc.EthanL()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Parameters setting
        port = 0
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])
        
        ## Open all pins and set it to digital output.
        err = dev.DO_openPort(port, timeout)
        print("DO_openPort:", err)

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i%2 == 0:
                value = [0,1,0,1,0,1,0,1]
            else:
                value = [1,0,1,0,1,0,1,0]

            dev.DO_writePort(port, value, timeout)
            print(f'Port: {port}, digital state = {value}')
            time.sleep(0.5)  ## delay(second)

        ## Close all pins with digital output
        err = dev.DO_closePort(port, timeout)
        print("DO_closePort:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()