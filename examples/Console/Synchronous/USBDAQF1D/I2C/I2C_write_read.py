'''
I2C - I2C_write_read.py with synchronous mode.

This example demonstrates how to communicate with USBDAQF1D. (master) and 24C08C (slave) with I2C interface.

First, it shows how to open I2C port and configure I2C parameters.
Second, write some bytes with address into EEPROM (24C08C). We have to make sure that bytes written in address is correct however read address from EEPROM (24C08C).
Last, close I2C port

The sensor used in this example is a 24C08C expecially for Two-wore Serial EEPROM.

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
    dev = pywpc.USBDAQF1D()

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
        port = 1 ## Depend on your device
        mode = 0
        device_address = 0x50 ## 01010000
        timeout = 3 ## second

        ## Generate random data
        import numpy as np
        word_address = np.random.randint(8) ## Generate a random address
        value = np.random.randint(256) ## Generate a random value

        '''
        Take 24C08C for example
        '''

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        '''
        Open I2C port
        '''

        ## Open I2C
        err = dev.I2C_open(port, timeout)
        print(f"I2C_open in port {port}: {err}")

        '''
        Set I2C parameter
        '''

        ## Set I2C port and set clock rate to standard mode
        err = dev.I2C_setClockRate(port, mode, timeout)
        print(f"I2C_setClockRate in port {port}: {err}")

        '''
        Write data via I2C
        '''

        ## Write data to device
        err = dev.I2C_write(port, device_address, [word_address, value], timeout)
        print(f"I2C_write in port {port}: {err}")
        print(f"write data: 0x{value:02X}")
        time.sleep(0.05) ## delay [s]

        '''
        Read data via I2C
        '''

        ## Write to set pointer for reading
        err = dev.I2C_write(port, device_address, [word_address], timeout)
        print(f"I2C_write in port {port}: {err}")

        ## Read data from device
        data = dev.I2C_read(port, device_address, 1, timeout)
        print(f"read data: 0x{data[0]:02X}")

        '''
        Close I2C port
        '''

        ## Close I2C
        err = dev.I2C_close(port, timeout)
        print(f"I2C_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()