##  example_SPI_read_and_write.py
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

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
        Take 25LC640 for example
        '''

        ## Parameters setting
        datasize = 0  ## Mode: 0 = 8-bit data, 1 = 16-bit data.
        first_bit = 0 ## Mode: 0 = MSB first, 1 = LSB first.
        prescaler = 64
        mode = 0    ## 0 : CPOL = 0 CPHA = 0 ## 1 : CPOL = 0 CPHA = 1  
                    ## 2 : CPOL = 1 CPHA = 0 ## 3 : CPOL = 1 CPHA = 1
        SPI_port = 1
        DO_port = 2 
        DO_index = [0] ## CS pin

        WRITE = 0x02
        DUMMY = 0x01
        READ = 0x03
        WREN = 0x06

        '''
        Open DO pins & SPI port & set CS(pin0) to high
        '''

        ## Open pin0 in port2 with digital output
        status = await dev.DO_openPins(DO_port, DO_index) 
        if status == 0: print("DO_openPins: OK")

        ## Open SPI port1
        status = await dev.SPI_open(SPI_port)
        if status == 0: print("SPI_open: OK")

        ## Set CS(pin0) to high
        status = await dev.DO_writePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writePins: OK")

        '''
        Set SPI parameter
        '''

        ## Set SPI port to 1 and set datasize to 8-bits data
        status = await dev.SPI_setDataSize(SPI_port, datasize)
        if status == 0: print("SPI_setDataSize: OK")
        
        ## Set SPI port to 1 and set first_bit to MSB first
        status = await dev.SPI_setFirstBit(SPI_port, first_bit)
        if status == 0: print("SPI_setFirstBit: OK")
        
        ## Set SPI port to 1 and set prescaler to 64
        status = await dev.SPI_setPrescaler(SPI_port, prescaler)
        if status == 0: print("SPI_setPrescaler: OK")
       
        ## Set SPI port to 1 and set CPOL and CPHA to 0 (mode 0)
        status = await dev.SPI_setMode(SPI_port, mode)
        if status == 0: print("SPI_setMode: OK")
        
        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        status = await dev.DO_writePins(DO_port, DO_index, [0]) 
        if status == 0: print("DO_writePins: OK")
        
        ## Write WREN byte
        status = await dev.SPI_write(SPI_port, [WREN])
        if status == 0: print("SPI_write: OK")

        ## Set CS(pin0) to high
        status = await dev.DO_writePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writePins: OK")

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        status = await dev.DO_writePins(DO_port, DO_index, [0]) 
        if status == 0: print("DO_writePins: OK") 
        
        ## Write data byte 0x0A in to address 0x0001
        status = await dev.SPI_write(SPI_port, [WRITE, 0x00, 0x01, 0x0A])
        if status == 0: print("SPI_write: OK")
        
        ## Set CS(pin0) to high
        status = await dev.DO_writePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writePins: OK")

        '''
        Read data via SPI
        '''

        ## Set CS(pin0) to low
        status = await dev.DO_writePins(DO_port, DO_index, [0]) 
        if status == 0: print("DO_writePins: OK")

        ## Read data byte 0x0A from address 0x0001
        data = await dev.SPI_readAndWrite(SPI_port, [READ, 0x00, 0x01, DUMMY])
        data = ['{:02x}'.format(value) for value in data]
        print("read data :", data)
       
        ## Set CS(pin0) to high
        status = await dev.DO_writePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writePins: OK")

        '''
        Close DO pins and SPI port
        '''

        ## Close SPI port1
        status = await dev.SPI_close(SPI_port)
        if status == 0: print("SPI_close: OK")

        ## Close pin0 in port2 with digital output
        status = await dev.DO_closePins(DO_port, DO_index) 
        if status == 0: print("DO_closePins: OK")
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