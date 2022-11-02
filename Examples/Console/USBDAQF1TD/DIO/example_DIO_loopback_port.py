
'''
DIO - example_DIO_loopback_port.py

This example demonstrates how to write DIO loopback in port from USBDAQF1TD.
Use DO pins to send signals and use DI pins to receive signals on single device also called "loopback".

First, it shows how to open DO and DI in port.
Second, write DO in port and read DI in port
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
    dev = pywpc.USBDAQF1TD()

    ## Connect to device
    try:
        dev.connect("21JA1239")
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port_DO = 0
        port_DI = 1

        ## Open all pins with digital output 
        status = await dev.DO_openPort_async(port_DO)
        print("DO_openPort_async status: ", status)

        ## Open all pins with digital input
        status = await dev.DI_openPort_async(port_DI)
        print("DI_openPort_async status: ", status)

        ## Set pin0, pin1 and pin2 to high, others to low
        status = await dev.DO_writePort_async(port_DO, [0,0,0,1,0,0,0,0])
        print("DO_writePort_async status: ", status)
        
        ## Read all pins state
        state_list = await dev.DI_readPort_async(port_DI)
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3)
        
        ## Close all pins with digital output
        status = await dev.DO_closePort_async(port_DO)
        print("DO_closePort_async status: ", status)
        
        ## Close all pins with digital input
        status = await dev.DI_closePort_async(port_DI)
        print("DI_closePort_async status: ", status)
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