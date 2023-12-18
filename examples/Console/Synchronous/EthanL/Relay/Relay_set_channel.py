'''
Relay - Relay_set_channel.py with synchronous mode.

This example demonstrates how to write channel from EthanL.

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
    dev = pywpc.EthanL()

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
        DO_port = 0
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Relay open
        err = dev.Relay_open(timeout)
        print(f"Relay_open: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            if i%2 == 0:
                value = [0, 0, 0, 0, 0, 0]
            else:
                value = [1, 1, 1, 1, 1, 1]

            dev.DO_writePort(DO_port, value, timeout)
            print(f'Port: {DO_port}, digital state= {value}')

            ## Wait
            time.sleep(0.5)  ## delay [s]

        ## Relay close
        err = dev.Relay_close(timeout)
        print(f"Relay_close: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()
