'''
SPI - SPI_write.py with asynchronous mode.

This example demonstrates how to communicate with USBDAQF1RD (master) and 25LC640 (slave) with SPI interface.

First, it shows how to open SPI port & DIO pins and configure SPI parameters.
Second, write some bytes with address into EEPROM (25LC640).
Last, close SPI port & DIO pins.

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
    dev = pywpc.USBDAQF1RD()

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
        Take 25LC640 for example
        '''

        ## Parameters setting
        port = 2 ## Depend on your device
        datasize = 0  ## Mode: 0 = 8-bit data, 1 = 16-bit data.
        first_bit = 0 ## Mode: 0 = MSB first, 1 = LSB first.
        prescaler = 64
        mode = 0    ## 0 : CPOL = 0 CPHA = 0 ## 1 : CPOL = 0 CPHA = 1
                    ## 2 : CPOL = 1 CPHA = 0 ## 3 : CPOL = 1 CPHA = 1

        if (port == 1){
            DO_port = 2
            DO_index = [0] ## CS pin
        }
        else if (port == 2){
            DO_port = 3
            DO_index = [2] ## CS pin
        }

        WRITE = 0x02
        WREN = 0x06

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        '''
        Open DO pins & SPI port & set CS(pin0) to high
        '''

        ## Open pin0 with digital output
        err = await dev.DO_openPins_async(DO_port, DO_index)
        print(f"DO_openPins_async in port {DO_port}: {err}")

        ## Open SPI
        err = await dev.SPI_open_async(port)
        print(f"SPI_open_async in port {port}: {err}")

        ## Set CS(pin0) to high
        err = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print(f"DO_writePins_async in port {DO_port}: {err}")

        '''
        Set SPI parameter
        '''

        ## Set SPI port and set datasize to 8-bits data
        err = await dev.SPI_setDataSize_async(port, datasize)
        print(f"SPI_setDataSize_async in port {port}: {err}")

        ## Set SPI port and set first_bit to MSB first
        err = await dev.SPI_setFirstBit_async(port, first_bit)
        print(f"SPI_setFirstBit_async in port {port}: {err}")

        ## Set SPI port and set prescaler to 64
        err = await dev.SPI_setPrescaler_async(port, prescaler)
        print(f"SPI_setPrescaler_async in port {port}: {err}")

        ## Set SPI port and set CPOL and CPHA to 0 (mode 0)
        err = await dev.SPI_setMode_async(port, mode)
        print(f"SPI_setMode_async in port {port}: {err}")

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        err = await dev.DO_writePins_async(DO_port, DO_index, [0])
        print(f"DO_writePins_async in port {DO_port}: {err}")

        ## Write WREN byte
        err = await dev.SPI_write_async(port, [WREN])
        print(f"SPI_write_async in port {port}: {err}")

        ## Set CS(pin0) to high
        err = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print(f"DO_writePins_async in port {DO_port}: {err}")

        '''
        Write data via SPI
        '''

        ## Set CS(pin0) to low
        err = await dev.DO_writePins_async(DO_port, DO_index, [0])
        print(f"DO_writePins_async in port {DO_port}: {err}")

        ## Write data byte 0x55 in to address 0x0002
        err = await dev.SPI_write_async(port, [WRITE, 0x00, 0x02, 0x55])
        print(f"SPI_write_async in port {port}: {err}")

        ## Set CS(pin0) to high
        err = await dev.DO_writePins_async(DO_port, DO_index, [1])
        print(f"DO_writePins_async in port {DO_port}: {err}")

        '''
        Close DO pins and SPI port
        '''

        ## Close SPI
        err = await dev.SPI_close_async(port)
        print(f"SPI_close_async in port {port}: {err}")

        ## Close pin0 with digital output
        err = await dev.DO_closePins_async(DO_port, DO_index)
        print(f"DO_closePins_async in port {DO_port}: {err}")
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