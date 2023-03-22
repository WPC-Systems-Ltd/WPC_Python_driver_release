'''
AO - AO_write_one_channel.py with asynchronous mode.

This example demonstrates how to write AO in specific channels from USBDAQF1AOD.

First, it shows how to open AO in port.
Second, write digital signals in specific channels.
Last, close AO in port.

Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AO
        err = await dev.AO_open_async(port)
        print(f"AO_open_async in port{port}: {err}")

        ## Set AO port and write data 1.5(V) in channel 4
        err = await dev.AO_writeOneChannel_async(port, 4, 1.5)
        print(f"AO_writeOneChannel_async in ch4 in port{port}: {err}")

        ## Set AO port and write data 2.5(V) in channel 5
        err = await dev.AO_writeOneChannel_async(port, 5, 2.5)
        print(f"AO_writeOneChannel_async in ch5 in port{port}: {err}")

        ## Set AO port and write data 3.5(V) in channel 6
        err = await dev.AO_writeOneChannel_async(port, 6, 3.5)
        print(f"AO_writeOneChannel_async in ch6 in port{port}: {err}")

        ## Set AO port and write data 4.5(V) in channel 7
        err = await dev.AO_writeOneChannel_async(port, 7, 4.5)
        print(f"AO_writeOneChannel_async in ch7 in port{port}: {err}")

        ## Close AO
        err = await dev.AO_close_async(port)
        print(f"AO_close_async in port{port}: {err}")
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
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder