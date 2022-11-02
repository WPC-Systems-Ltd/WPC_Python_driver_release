
'''
DIO - example_DO_write_port.py

This example demonstrates how to write DO in port from EthanD.

First, it shows how to open DO in port.
Second, write DO pins in two different types (hex or list) but it should be consistency.
Last, close DO in port.

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
    dev = pywpc.EthanD()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0
        
        ## Open all pins and set it to digital output
        status = await dev.DO_openPort_async(port)
        print("DO_openPort_async status: ", status)
        
        ## Set pin0, pin3 and pin4 to high, others to low
        status = await dev.DO_writePort_async(port, [0,0,0,1,1,0,0,1])
        print("DO_writePort_async status: ", status)

        ## Wait for 5 second
        await asyncio.sleep(5)  ## delay(second)

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        status = await dev.DO_writePort_async(port, 0xC0)
        print("DO_writePort_async status: ", status)
       
        ## Wait for 1 second
        await asyncio.sleep(1)  ## delay(second)

        ## Close all pins with digital output
        status = await dev.DO_closePort_async(port)
        print("DO_closePort_async status: ", status)
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