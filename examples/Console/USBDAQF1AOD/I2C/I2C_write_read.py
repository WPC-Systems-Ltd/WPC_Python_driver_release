'''
I2C - I2C_write_read.py

This example demonstrates how to communicate with USBDAQF1AOD. (master) and 24C08C (slave) with I2C interface.

First, it shows how to open I2C port and configure I2C parameters.
Second, write some bytes with address into EEPROM (24C08C). We have to make sure that bytes written in address is correct however read address from EEPROM (24C08C).
Last, close I2C port

The sensor used in this example is a 24C08C expecially for Two-wore Serial EEPROM.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

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
        status = await dev.I2C_open_async(I2C_port)
        print("I2C_open_async status: ", status)

        '''
        Set I2C parameter
        '''

        ## Set I2C port and set clock rate to standard mode
        status = await dev.I2C_setClockRate_async(I2C_port, mode)
        print("I2C_setClockRate_async status: ", status)

        '''
        Write data via I2C
        '''

        ## Write WREN byte
        status = await dev.I2C_write_async(I2C_port, device_address, [word_address, 0xAA, 0x55, 0xAA, 0x55])
        print("I2C_write_async status: ", status)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        '''
        Read data via I2C
        '''

        status = await dev.I2C_write_async(I2C_port, device_address, [word_address])
        print("I2C_write_async status: ", status)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        data_list = await dev.I2C_read_async(I2C_port, device_address, 4)
        print("read data :", data_list)

        '''
        Close I2C port
        '''

        ## Close I2C
        status = await dev.I2C_close_async(I2C_port)
        print("I2C_close_async status: ", status)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())