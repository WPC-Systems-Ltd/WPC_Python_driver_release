'''
I2C - I2C_write_read.py

This example demonstrates how to communicate with USBDAQF1CD. (master) and 24C08C (slave) with I2C interface.

First, it shows how to open I2C port and configure I2C parameters.
Second, write some bytes with address into EEPROM (24C08C). We have to make sure that bytes written in address is correct however read address from EEPROM (24C08C).
Last, close I2C port

The sensor used in this example is a 24C08C expecially for Two-wore Serial EEPROM.

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
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("21JA1312")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        '''
        Take 24C08N for example
        '''

        ## Parameters setting
        I2C_port = 1
        mode = 0
        device_address = 0x50 ## 01010000
        word_address = 0x00

        '''
        Open I2C port
        '''

        ## Open I2C
        err = dev.I2C_open(I2C_port)
        print("I2C_open:", err)

        '''
        Set I2C parameter
        '''

        ## Set I2C port and set clock rate to standard mode
        err = dev.I2C_setClockRate(I2C_port, mode)
        print("I2C_setClockRate:", err)

        '''
        Write data via I2C
        '''

        ## Write WREN byte
        err = dev.I2C_write(I2C_port, device_address, [word_address, 0xAA, 0x55, 0xAA, 0x55])
        print("I2C_write:", err)

        '''
        Read data via I2C
        '''

        err = dev.I2C_write(I2C_port, device_address, [word_address])
        print("I2C_write:", err)

        data_list = dev.I2C_read(I2C_port, device_address, 4)
        print("read data :", data_list)

        '''
        Close I2C port
        '''

        ## Close I2C
        err = dev.I2C_close(I2C_port)
        print("I2C_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()