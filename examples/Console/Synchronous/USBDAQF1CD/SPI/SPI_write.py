'''
SPI - SPI_write.py with synchronous mode.

This example demonstrates how to communicate with USBDAQF1CD (master) and 25LC640 (slave) with SPI interface.

First, it shows how to open SPI port & DIO pins and configure SPI parameters.
Second, write some bytes with address into EEPROM (25LC640).
Last, close SPI port & DIO pins.

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
        ## Parameters setting
        datasize = 0  ## Mode: 0 = 8-bit data, 1 = 16-bit data.
        first_bit = 0 ## Mode: 0 = MSB first, 1 = LSB first.
        prescaler = 64
        mode = 0    ## 0 : CPOL = 0 CPHA = 0 ## 1 : CPOL = 0 CPHA = 1
                    ## 2 : CPOL = 1 CPHA = 0 ## 3 : CPOL = 1 CPHA = 1
        SPI_port = 2
        DO_port = 0
        DO_index = [0] ## CS pin
        timeout = 3  ## second

        WRITE = 0x02
        WREN = 0x06

        '''
        Take 25LC640 for example
        '''

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        '''
        Open DO pins & SPI port & set CS(pin0) to high
        '''

        ## Open pin0 with digital output
        err = dev.DO_openPins(DO_port, DO_index, timeout)
        print("DO_openPins:", err)

        ## Open SPI
        err = dev.SPI_open(SPI_port, timeout)
        print("SPI_open:", err)

        ## Set CS(pin0) to high
        err = dev.DO_writePins(DO_port, DO_index, [1], timeout)
        print("DO_writePins:", err)

        '''
        Set SPI parameter
        '''

        ## Set SPI port and set datasize to 8-bits data
        err = dev.SPI_setDataSize(SPI_port, datasize, timeout)
        print("SPI_setDataSize:", err)

        ## Set SPI port and set first_bit to MSB first
        err = dev.SPI_setFirstBit(SPI_port, first_bit, timeout)
        print("SPI_setFirstBit:", err)

        ## Set SPI port and set prescaler to 64
        err = dev.SPI_setPrescaler(SPI_port, prescaler, timeout)
        print("SPI_setPrescaler:", err)

        ## Set SPI port and set CPOL and CPHA to 0 (mode 0)
        err = dev.SPI_setMode(SPI_port, mode, timeout)
        print("SPI_setMode:", err)

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        err = dev.DO_writePins(DO_port, DO_index, [0], timeout)
        print("DO_writePins:", err)

        ## Write WREN byte
        err = dev.SPI_write(SPI_port, [WREN], timeout)
        print("SPI_write:", err)

        ## Set CS(pin0) to high
        err = dev.DO_writePins(DO_port, DO_index, [1], timeout)
        print("DO_writePins:", err)

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        err = dev.DO_writePins(DO_port, DO_index, [0], timeout)
        print("DO_writePins:", err)

        ## Write data byte 0x55 in to address 0x0002
        err = dev.SPI_write(SPI_port, [WRITE, 0x00, 0x02, 0x55], timeout)
        print("SPI_write:", err)

        ## Set CS(pin0) to high
        err = dev.DO_writePins(DO_port, DO_index, [1], timeout)
        print("DO_writePins:", err)

        '''
        Close DO pins and SPI port
        '''

        ## Close SPI
        err = dev.SPI_close(SPI_port)
        print("SPI_close:", err)

        ## Close pin0 with digital output
        err = dev.DO_closePins(DO_port, DO_index)
        print("DO_closePins:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
    
if __name__ == '__main__':
    main()