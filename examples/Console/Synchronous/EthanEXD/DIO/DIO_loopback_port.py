'''
DIO - DIO_loopback_port.py with synchronous mode.

This example demonstrates the process of DIO loopback using port from EthanEXD.
It involves using DO port to send signals and DI port to receive signals on a single device, commonly known as "loopback".

To begin with, it illustrates the steps required to open the DO and DI port.
Next, it performs the operation of writing to a DO pin and reading from a DI pin.
Lastly, it concludes by closing the DO and DI port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanEXD()

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
        DO_port = 0 ## Depend on your device
        DI_port = 2
        DO_value = [1, 0, 1, 0]
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open DO port with digital output
        err = dev.DO_openPort(DO_port, timeout)
        print(f"DO_openPort in DO_port {DO_port}: {err}")

        ## Open DI port with digital input
        err = dev.DI_openPort(DI_port, timeout)
        print(f"DI_openPort in DI_port {DI_port}: {err}")

        ## Write DO port to high or low
        err = dev.DO_writePort(DO_port, DO_value, timeout)
        print(f"DO_writePort in DO_port {DO_port}: {err}")

        ## Read DI port state
        state_list = dev.DI_readPort(DI_port, timeout)
        print(f"state_list in DI_port {DI_port}: {state_list}")

        ## Close DO port with digital output
        err = dev.DO_closePort(DO_port, timeout)
        print(f"DO_closePort in DO_port {DO_port}: {err}")

        ## Close DI port with digital input
        err = dev.DI_closePort(DI_port, timeout)
        print(f"DI_closePort in DI_port {DI_port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()