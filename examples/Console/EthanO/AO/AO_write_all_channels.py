'''
AO - AO_write_all_channels.py

This example demonstrates how to write AO in all channels from EthanO.

First, it shows how to open AO in port.
Second, write all digital signals
Last, close AO in port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanO()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0

        ## Open AO
        err = await dev.AO_open_async(port)
        print("AO_open_async:", err)

        ## Set AO port and write data simultaneously
        err = await dev.AO_writeAllChannels_async(port, [0,1,2,3,4,5,4,3])
        print("AO_writeAllChannels_async:", err)

        ## Sleep
        await asyncio.sleep(1) ## delay(second)

        ## Close AO
        err = await dev.AO_close_async(port)
        print("AO_close_async:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return

if __name__ == '__main__':
    asyncio.run(main())