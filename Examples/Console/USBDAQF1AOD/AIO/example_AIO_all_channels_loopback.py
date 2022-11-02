
'''
AIO - example_AIO_all_channels_loopback.py

This example demonstrates how to write AIO loopback in all channels from USBDAQF1AOD.
Use AO pins to send signals and use AI pins to receive signals on single device also called "loopback".

First, it shows how to open AO and AI in port.
Second, write all digital signals to AO and read AI ondemand data.
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

        ## Open AI
        status = await dev.AI_open_async(port)
        print("AI_open_async status: ", status)
        
        ## Open AO
        status = await dev.AO_open_async(port)
        print("AO_open_async status: ", status)

        ## Set AI port and data acquisition
        data = await dev.AI_readOnDemand_async(port)
        print("data :" + str(data))

        ## Set AO port and write data simultaneously
        status = await dev.AO_writeAllChannels_async(port, [0,1,2,3,4,5,4,3])
        print("AO_writeAllChannels_async status: ", status)

        ## Sleep
        await asyncio.sleep(1) ## delay(second)

        ## Set AI port and data acquisition
        data = await dev.AI_readOnDemand_async(port)
        print("data :" + str(data))

        ## Close AI
        status = await dev.AI_close_async(port) 
        print("AI_close_async status: ", status)

        ## Close AO
        status = await dev.AO_close_async(port) 
        print("AO_close_async status: ", status)
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