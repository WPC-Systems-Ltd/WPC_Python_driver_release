'''
UART - UART_write.py

This example demonstrates how to write data to another device with UART interface from USBDAQF1AD.

First, it shows how to open UART port and configure UART parameters.
Second, write bytes to another device.
Last, close UART port.

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
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("21JA1245")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Parameters setting
        port = 2
        baudrate = 9600
        data_bit_mode = 0  ## 0 : 8-bit data, 1 : 9-bit data.
        parity_mode = 0    ## 0 : None, 2 : Even parity, 3 : Odd parity.
        stop_bit_mode = 0  ## 0 : 1 bit, 1 : 0.5 bits, 2 : 2 bits, 3 : 1.5 bits
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Open UART
        err = dev.UART_open(port, timeout)
        print("UART_open:", err)

        ## Set UART port and set baudrate to 9600
        err = dev.UART_setBaudRate(port, baudrate, timeout)
        print("UART_setBaudRate:", err)

        ## Set UART port and set data bit to 8-bit data
        err = dev.UART_setDataBit(port, data_bit_mode, timeout)
        print("UART_setDataBit:", err)

        ## Set UART port and set parity to None
        err = dev.UART_setParity(port, parity_mode, timeout)
        print("UART_setParity:", err)

        ## Set UART port and set stop bit to 1 bit
        err = dev.UART_setNumStopBit(port, stop_bit_mode, timeout)
        print("UART_setNumStopBit:", err)

        ## Set UART port and and write "12345" to device in string format
        err = dev.UART_write(port, "12345", timeout)
        print("UART_write:", err)

        ## Set UART port and and write "chunglee people" to device
        err = dev.UART_write(port, "chunglee people", timeout)
        print("UART_write:", err)

        ## Set UART port and and write "12345" to device in list format
        err = dev.UART_write(port, ["1","2","3","4","5"], timeout)
        print("UART_write:", err)

        ## Close UART
        err = dev.UART_close(port, timeout)
        print("UART_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()