'''
AO - example_AO_write_all_channels.py

This example demonstrates how to write AO in all channels from WPC-USB-DAQ-F1-AOD.

First, it shows how to open AO in port.
Second, write all digital signals
Last, close AO in port.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio
import sys
 
## WPC
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc  

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
 
        ## Open AO port0
        status = await dev.AO_open(port)
        if status == 0: print("AO_open: OK")
 
        ## Set AO port to 0 and write data simultaneously
        status = await dev.AO_writeAllChannels(port, [0,1,2,3,4,5,4,3])
        if status == 0: print("AO_writeAllChannels: OK")

        ## Sleep
        await asyncio.sleep(1) ## delay(second)
 
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
