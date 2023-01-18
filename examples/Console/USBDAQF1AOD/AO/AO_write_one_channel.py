'''
AO - AO_write_one_channel.py

This example demonstrates how to write AO in specific channels from USBDAQF1AOD.

First, it shows how to open AO in port.
Second, write digital signals in specific channels.
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
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("21JA1439")
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

        ## Set AO port and write data 1.5(V) in channel 4
        err = await dev.AO_writeOneChannel_async(port, 4, 1.5)
        print("AO_writeOneChannel_async:", err)

        ## Set AO port and write data 2.5(V) in channel 5
        err = await dev.AO_writeOneChannel_async(port, 5, 2.5)
        print("AO_writeOneChannel_async:", err)

        ## Set AO port and write data 3.5(V) in channel 6
        err = await dev.AO_writeOneChannel_async(port, 6, 3.5)
        print("AO_writeOneChannel_async:", err)

        ## Set AO port and write data 4.5(V) in channel 7
        err = await dev.AO_writeOneChannel_async(port, 7, 4.5)
        print("AO_writeOneChannel_async:", err)

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

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))

if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)， 
    # main_for_spyder ## Use Spyder