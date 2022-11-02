
'''
CAN - example_CAN_read.py

This example demonstrates how to read data from another device with CAN interface from USBDAQF1CD.

First, it shows how to open CAN port and configure CAN parameters.
Second, read bytes from another device.
Last, stop and close CAN port.

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

    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("21JA1320")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get Firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port  = 1
        speed = 0 ## 0 = 125 KHz, 1 = 250 kHz, 2 = 500 kHz, 3 = 1 MHz

        ## Open CAN
        status = await dev.CAN_open_async(port) 
        print("CAN_open_async status: ", status)

        ## Set CAN port and set speed to 0  
        status = await dev.CAN_setSpeed_async(port, speed) 
        print("CAN_setSpeed_async status: ", status)

        ## Set CAN port and start CAN
        status = await dev.CAN_start_async(port) 
        print("CAN_start_async status: ", status)

        ## Read 5 frames for 1000 times
        for i in range(1000):
            data = await dev.CAN_read_async(port, 5)
            if data is None:
                await asyncio.sleep(0.01)
            else:
                print(data)
            
        ## Set CAN port and stop CAN  
        status = await dev.CAN_stop_async(port) 
        print("CAN_stop_async status: ", status)
        
        ## Close CAN 
        status = await dev.CAN_close_async(port) 
        print("CAN_close_async status: ", status)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())