'''
Find_devices - find_network_devices_blink.py with asynchronous mode.

This example demonstrates how to find ethernet devices and blink.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.DeviceFinder()

    ## Connect to device
    dev.connect()

    ## Perform network device information
    print("Find all network devices....")
    try:
        dev_2d_list = await dev.Bcst_enumerateNetworkDevices_async()
        for device_list in dev_2d_list:
            print(device_list)
            mac_num = device_list[2]

            ## Check MAC and let LED blink
            err = async dev.Bcst_checkMACAndRing_async(mac_num)
            print(f"Bcst_checkMACAndRing_async, status: {err}")

    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect to device
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