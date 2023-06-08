'''
UART - UART_read.py with synchronous mode.

This example demonstrates how to read data from another device with UART interface from USBDAQF1AOD.

First, it shows how to open UART port and configure UART parameters.
Second, read bytes from another device.
Last, close UART port.

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
        port = 2 ## Depend on your device
        baudrate = 9600
        data_bit_mode = 0  ## 0 : 8-bit data, 1 : 9-bit data.
        parity_mode = 0    ## 0 : None, 2 : Even parity, 3 : Odd parity.
        stop_bit_mode = 0  ## 0 : 1 bit, 1 : 0.5 bits, 2 : 2 bits, 3 : 1.5 bits
        timeout = 3  ## second
        read_bytes = 20
        delay = 0.005 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open UART
        err = dev.UART_open(port, timeout=timeout)
        print(f"UART_open in port {port}: {err}")

        ## Set UART port and set baudrate to 9600
        err = dev.UART_setBaudRate(port, baudrate, timeout=timeout)
        print(f"UART_setBaudRate in port {port}: {err}")

        ## Set UART port and set data bit to 8-bit data
        err = dev.UART_setDataBit(port, data_bit_mode, timeout=timeout)
        print(f"UART_setDataBit in port {port}: {err}")

        ## Set UART port and set parity to None
        err = dev.UART_setParity(port, parity_mode, timeout=timeout)
        print(f"UART_setParity in port {port}: {err}")

        ## Set UART port and set stop bit to 8-bit data
        err = dev.UART_setNumStopBit(port, stop_bit_mode, timeout=timeout)
        print(f"UART_setNumStopBit in port {port}: {err}")

        ## Print informaion
        print("Wait for 10 seconds to receive data from other devices")

        ## Wait
        time.sleep(10) ## delay [s]

        ## Set UART port and read 20 bytes
        data = dev.UART_read(port, read_bytes, delay=delay)
        print(f"data in port {port}: {data}")

        ## Close UART
        err = dev.UART_close(port, timeout=timeout)
        print(f"UART_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()