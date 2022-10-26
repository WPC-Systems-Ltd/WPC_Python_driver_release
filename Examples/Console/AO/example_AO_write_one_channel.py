'''
AO - example_AO_write_one_channel.py

This example demonstrates how to write AO in specific channels from WPC-USB-DAQ-F1-AOD.

First, it shows how to open AO in port.
Second, write digital signals in specific channels.
Last, close AO in port.

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
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0

        ## Open AO port0
        status = await dev.AO_open_async(port)
        if status == 0: print("AO_open: OK")

        ## Set AO port to 0 and write data 1.5(V) in channel 4 
        status = await dev.AO_writeOneChannel_async(port, 4, 1.5)
        if status == 0: print("AO_writeOneChannel: OK")
        
        ## Set AO port to 0 and write data 2.5(V) in channel 5 
        status = await dev.AO_writeOneChannel_async(port, 5, 2.5)
        if status == 0: print("AO_writeOneChannel: OK")
        
        ## Set AO port to 0 and write data 3.5(V) in channel 6 
        status = await dev.AO_writeOneChannel_async(port, 6, 3.5)
        if status == 0: print("AO_writeOneChannel: OK")
        
        ## Set AO port to 0 and write data 4.5(V) in channel 7 
        status = await dev.AO_writeOneChannel_async(port, 7, 4.5)
        if status == 0: print("AO_writeOneChannel: OK")

        ## Sleep
        await asyncio.sleep(1) ## delay(second)
        
        ## Close AO port0
        status = await dev.AO_close_async(port) 
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
