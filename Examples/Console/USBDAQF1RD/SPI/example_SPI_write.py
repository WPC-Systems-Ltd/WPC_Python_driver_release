
'''
SPI - example_SPI_write.py

This example demonstrates how to communicate with USBDAQF1RD (master) and 25LC640 (slave) with SPI interface.

First, it shows how to open SPI port & DIO pins and configure SPI parameters.
Second, write some bytes with address into EEPROM (25LC640).
Last, close SPI port & DIO pins

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio

## WPC
try:
    from wpcsys import pywpc
except:
    import sys
    sys.path.insert(0, 'src/')
    import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("21JA1385")
    except Exception as err:
        pywpc.printGenericError(err)
        
    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        '''
        Take 25LC640 for example
        '''

        ## Parameters setting
        datasize = 0  ## Mode: 0 = 8-bit data, 1 = 16-bit data.
        first_bit = 0 ## Mode: 0 = MSB first, 1 = LSB first.
        prescaler = 64
        mode = 0    ## 0 : CPOL = 0 CPHA = 0 ## 1 : CPOL = 0 CPHA = 1  
                    ## 2 : CPOL = 1 CPHA = 0 ## 3 : CPOL = 1 CPHA = 1
        SPI_port = 2
        DO_port = 0 
        DO_index = [0] ## CS pin

        WRITE = 0x02
        WREN = 0x06

        '''
        Open DO pins & SPI port & set CS(pin0) to high
        '''

        ## Open pin0 with digital output
        status = await dev.DO_openPins_async(DO_port, DO_index) 
        print("DO_openPins_async status: ", status)

        ## Open SPI
        status = await dev.SPI_open_async(SPI_port)
        print("SPI_open_async status: ", status)
        
        ## Set CS(pin0) to high
        status = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print("DO_writePins_async status: ", status)

        '''
        Set SPI parameter
        '''

        ## Set SPI port and set datasize to 8-bits data
        status = await dev.SPI_setDataSize_async(SPI_port, datasize)
        print("SPI_setDataSize_async status: ", status)
        
        ## Set SPI port and set first_bit to MSB first
        status = await dev.SPI_setFirstBit_async(SPI_port, first_bit)
        print("SPI_setFirstBit_async status: ", status)
        
        ## Set SPI port and set prescaler to 64
        status = await dev.SPI_setPrescaler_async(SPI_port, prescaler)
        print("SPI_setPrescaler_async status: ", status)
       
        ## Set SPI port and set CPOL and CPHA to 0 (mode 0)
        status = await dev.SPI_setMode_async(SPI_port, mode)
        print("SPI_setMode_async status: ", status)

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        status = await dev.DO_writePins_async(DO_port, DO_index, [0]) 
        print("DO_writePins_async status: ", status)
        
        ## Write WREN byte
        status = await dev.SPI_write_async(SPI_port, [WREN])
        print("SPI_write_async status: ", status)

        ## Set CS(pin0) to high
        status = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print("DO_writePins_async status: ", status)

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        status = await dev.DO_writePins_async(DO_port, DO_index, [0]) 
        print("DO_writePins_async status: ", status)
        
        ## Write data byte 0x55 in to address 0x0002
        status = await dev.SPI_write_async(SPI_port, [WRITE, 0x00, 0x02, 0x55])
        print("SPI_write_async status: ", status)
        
        ## Set CS(pin0) to high
        status = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print("DO_writePins_async status: ", status)
 
        '''
        Close DO pins and SPI port
        '''

        ## Close SPI
        status = await dev.SPI_close_async(SPI_port)
        print("SPI_close_async status: ", status)

        ## Close pin0 with digital output
        status = await dev.DO_closePins_async(DO_port, DO_index) 
        print("DO_closePins_async status: ", status)
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