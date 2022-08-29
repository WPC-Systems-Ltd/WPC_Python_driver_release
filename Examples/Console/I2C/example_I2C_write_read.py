'''
I2C - example_I2C_write_read.py

example_I2C_write_read that demonstrates how to initialize and set parameters I2C with USB-DAQ-F1-D
as well as reading and writing from and to registers for a sensor connected over I2C.

The sensor used in this example is a 24C08C expecially for Two-wore Serial EEPROM

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio
import sys
 
## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to USB device
    try:
        dev.connect("21JA1279")
    except Exception as err:
        pywpc.printGenericError(err)
        
    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
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

        ## Open I2C port1
        status = await dev.I2C_open(I2C_port)
        if status == 0: print("I2C_open: OK")
        
        '''
        Set I2C parameter
        '''

        ## Set I2C port to 1 and set clock rate to standard mode
        status = await dev.I2C_setClockRate(I2C_port, mode)
        if status == 0: print("I2C_setClockRate: OK")

        '''
        Write data via I2C
        '''
        
        ## Write WREN byte
        status = await dev.I2C_write(I2C_port, device_address, [word_address, 0xAA, 0x55, 0xAA, 0x55])
        if status == 0: print("I2C_write: OK")
        
        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        '''
        Read data via I2C
        '''

        status = await dev.I2C_write(I2C_port, device_address, [word_address])
        if status == 0: print("I2C_write: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        data_list = await dev.I2C_read(I2C_port, device_address, 4)
        print("read data :", data_list)
       
        '''
        Close I2C port
        ''' 

        ## Close I2C port1
        status = await dev.I2C_close(I2C_port)
        if status == 0: print("I2C_close: OK")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return
    
if __name__ == '__main__':
    asyncio.run(main())