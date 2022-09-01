'''
AIO - example_AIO_one_channel_loopback.py

This example demonstrates how to write AIO loopback in specific channel from WPC-USB-DAQ-F1-AOD.
Use AO pins to send signals and use AI pins to receive signals on single device also called "loopback".

First, it shows how to open AO and AI in port.
Second, write digital signals to AO in specific channel and read AI ondemand data.
Last, close AO and AI in port.

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

    ## Connect to USB device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)
        
    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0

        ## Open AI port 0
        status = await dev.AI_open(port)
        if status == 0: print("AI_open: OK")
        
        ## Open AO port0
        status = await dev.AO_open(port)
        if status == 0: print("AO_open: OK")

        ## Set AI port to 0 and data acquisition
        data = await dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Set AO port to 0 and write data 1.5(V) in channel 4 
        status = await dev.AO_writeOneChannel(port, 4, 1.5)
        if status == 0: print("AO_writeByChannels: OK")
        
        ## Set AO port to 0 and write data 2.5(V) in channel 5 
        status = await dev.AO_writeOneChannel(port, 5, 2.5)
        if status == 0: print("AO_writeByChannels: OK")
        
        ## Set AO port to 0 and write data 3.5(V) in channel 6 
        status = await dev.AO_writeOneChannel(port, 6, 3.5)
        if status == 0: print("AO_writeByChannels: OK")
        
        ## Set AO port to 0 and write data 4.5(V) in channel 7 
        status = await dev.AO_writeOneChannel(port, 7, 4.5)
        if status == 0: print("AO_writeByChannels: OK")

        ## Sleep
        await asyncio.sleep(1) ## delay(second)

        ## Set AI port to 0 and data acquisition
        data = await dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Close AI port0
        status = await dev.AI_close(port) 
        if status == 0: print("AI_close: OK")

        ## Close AO port0
        status = await dev.AO_close(port) 
        if status == 0: print("AO_close: OK") 
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
