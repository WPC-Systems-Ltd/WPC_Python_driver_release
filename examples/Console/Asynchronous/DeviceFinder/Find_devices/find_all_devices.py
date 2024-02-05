'''
Find_devices - find_all_devices.py with asynchronous mode.

This example demonstrates how to find all available USB and ethernet devices.

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
    dev = pywpc.DeviceFinder()

    ## Connect to device
    dev.connect()

    ## Perform USB device information
    print("Find all USB devices....")
    try:
        dev_list = dev.Bcst_enumerateUSBDevices()
        for device in dev_list:
            print(device)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform network device information
    print("Find all network devices....")
    try:
        dev_list = await dev.Bcst_enumerateNetworkDevices_async()
        for device in dev_list:
            print(device)
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