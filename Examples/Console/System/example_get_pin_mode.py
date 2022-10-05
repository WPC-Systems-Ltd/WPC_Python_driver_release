'''
System - example_get_pin_mode.py

This example demonstrates how to get pin mode from WPC-USB-DAQ-F1-D.

First, get idle pin mode and show how to open DO and DI in pins.
Second, get idle pin mode and set port idle mode. Again, get pin mode.
Last, close DO and DI in port.

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

    ## Connect to USB device
    try:
        dev.connect('21JA1439')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            ## Get pin mode
            pin_mode = await dev.Sys_getPinModeInPort_async(i)
            print("pin_mode", pin_mode)

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)
        print()
        print("====================")

        ## Parameters setting
        port_DO = 0
        port_DI = 1
        
        ## Open pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output
        await dev.DO_openPins_async(port_DO, [0,1,2,3,4])

        ## Set pin0, pin3 and pin4 to digital high, others to digital low
        await dev.DO_writeValuePins(port_DO, [0,1,2,3,4], [1,0,0,1,1]) 

        ## Open pin4, pin5, pin6 and pin7 in port 1 with digital input 
        await dev.DI_openPins_async(port_DI, [4,5,6,7])

        ## Get pinmode from port 0 to port 3
        for i in range(4):
            ## Get pin mode
            pin_mode = await dev.Sys_getPinModeInPort_async(i)
            print("pin_mode", pin_mode)

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 1 seconds
        await asyncio.sleep(1)  ## delay(second)

        ## Set port 0 to idle
        await dev.Sys_setPortIdle_async(0)
        print()
        print("====================")
                
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            ## Get pin mode
            pin_mode = await dev.Sys_getPinModeInPort_async(i)
            print("pin_mode", pin_mode)

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

        ## Close pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output 
        await dev.DO_closePins_async(port_DO, [0,1,2,3,4])

        ## Close pin4, pin5, pin6 and pin7 in port 1 with digital input
        await dev.DI_closePins_async(port_DI, [4,5,6,7])
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