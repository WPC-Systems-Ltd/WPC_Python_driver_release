'''
I2C - I2C_write_read.py with asynchronous mode.

This example demonstrates how to communicate with USBDAQF1AD. (master) and 24C08C (slave) with I2C interface.

First, it shows how to open I2C port and configure I2C parameters.
Second, write some bytes with address into EEPROM (24C08C). We have to make sure that bytes written in address is correct however read address from EEPROM (24C08C).
Last, close I2C port

The sensor used in this example is a 24C08C expecially for Two-wore Serial EEPROM.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        '''
        Take 24C08C for example
        '''

        ## Parameters setting
        port = 1 ## Depend on your device
        port = 1 ## Depend on your device
        mode = 0
        device_address = 0x50 ## 01010000
        word_address = 0x00

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        '''
        Open I2C port
        '''

        ## Open I2C
        err = await dev.I2C_open_async(port)
        print(f"I2C_open_async in port {port}: {err}")

        '''
        Set I2C parameter
        '''

        ## Set I2C port and set clock rate to standard mode
        err = await dev.I2C_setClockRate_async(port, mode)
        print(f"I2C_setClockRate_async in port {port}: {err}")

        '''
        Write data via I2C
        '''

        ## Write WREN byte
        err = await dev.I2C_write_async(port, device_address, [word_address, 0xAA, 0x55, 0xAA, 0x55])
        print(f"I2C_write_async in port {port}: {err}")

        '''
        Read data via I2C
        '''

        err = await dev.I2C_write_async(port, device_address, [word_address])
        print(f"I2C_write_async in port {port}: {err}")

        data_list = await dev.I2C_read_async(port, device_address, 4)
        print("read data :", data_list)

        '''
        Close I2C port
        '''

        ## Close I2C
        err = await dev.I2C_close_async(port)
        print(f"I2C_close_async in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))

if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder