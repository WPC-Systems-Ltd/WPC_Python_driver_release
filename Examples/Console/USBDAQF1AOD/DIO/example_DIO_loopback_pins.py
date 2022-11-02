
'''
DIO - example_DIO_loopback_pins.py

This example demonstrates how to write DIO loopback in pins from USBDAQF1AOD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in pins.
Second, write DO pin and read DI pin
Last, close DO and DI in pins.

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
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0
        
        ## Open pin0, pin1, pin2, pin3 and pin4 with digital output
        status = await dev.DO_openPins_async(port, [0,1,2,3,4]) 
        print("DO_openPins_async status: ", status)
        
        ## Set pin0 and pin1 to high, others to low
        await dev.DO_writePins_async(port, [0,1,2,3,4], [1,1,0,0,0]) 
        print("DO_writePins_async status: ", status)

        ## Open pin5, pin6 and pin7 with digital output
        status = await dev.DI_openPins_async(port, [5,6,7])
        print("DI_openPins_async status: ", status)

        ## Read pin5, pin6 and pin7 state
        state_list = await dev.DI_readPins_async(port, [7,5,6])
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3) ## delay(second)

        ## Close pin0, pin1, pin2, pin3 and pin4 with digital output 
        status = await dev.DO_closePins_async(port, [0,1,2,3,4])
        print("DO_closePins_async status: ", status)

        ## Close pin5, pin6 and pin7 with digital input
        status = await dev.DI_closePins_async(port, [5,6,7])
        print("DI_closePins_async status: ", status)
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