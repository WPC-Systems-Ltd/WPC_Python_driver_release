'''
DPOT - DPOT_readByChannel.py with asynchronous mode.

This example demonstrates how to read digital potentiometer resistance by channel from EthanP.
-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanP()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
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

        ## Open DPOT
        err = await dev.DPOT_open_async(port)
        print(f"DPOT_open_async in port {port}, status: {err}")

        ## Read all channels by for loop
        for i in range(4):
            resistance_ratio = await dev.DPOT_readByChannel_async(i)
            print(f"resistance_ratio in channel {i}: {resistance_ratio}")

        ## Close DPOT
        err = await dev.DPOT_close_async(port)
        print(f"DPOT_close_async in port {port}, status: {err}")

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