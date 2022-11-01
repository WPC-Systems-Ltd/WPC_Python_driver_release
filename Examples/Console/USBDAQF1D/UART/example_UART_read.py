
'''
UART - example_UART_read.py

This example demonstrates how to read data from another device with UART interface from USBDAQF1D.

First, it shows how to open UART port and configure UART parameters.
Second, read bytes from another device.
Last, close UART port.

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
    dev = pywpc.USBDAQF1D()

    ## Connect to device
    try:
        dev.connect("21JA1200")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 2
        baudrate = 9600 
        data_bit_mode = 0  ## 0 : 8-bit data, 1 : 9-bit data.
        parity_mode = 0    ## 0 : None, 2 : Even parity, 3 : Odd parity.
        stop_bit_mode = 0  ## 0 : 1 bit, 1 : 0.5 bits, 2 : 2 bits, 3 : 1.5 bits  
       
        ## Open UART
        status = await dev.UART_open_async(port) 
        print("UART_open_async status: ", status)

        ## Set UART port and set baudrate to 9600
        status = await dev.UART_setBaudRate_async(port, baudrate)
        print("UART_setBaudRate_async status: ", status)
 
        ## Set UART port and set data bit to 8-bit data
        status = await dev.UART_setDataBit_async(port, data_bit_mode)
        print("UART_setDataBit_async status: ", status)
        
        ## Set UART port and set parity to None
        status = await dev.UART_setParity_async(port, parity_mode)
        print("UART_setParity_async status: ", status)

        ## Set UART port and set stop bit to 8-bit data
        status = await dev.UART_setNumStopBit_async(port, stop_bit_mode)
        print("UART_setNumStopBit_async status: ", status)

        ## Sleep
        await asyncio.sleep(10) ## delay(second)
        
        ## Set UART port and read 20 bytes
        data = await dev.UART_read_async(port, 20) 
        print("data: ", data)

        ## Close UART
        status = await dev.UART_close_async(port) 
        print("UART_close_async status: ", status)
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