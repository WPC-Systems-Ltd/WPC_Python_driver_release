'''
SD - SD_write.py with asynchronous mode.

This example demonstrates how to read a message from SD card from WifiDAQE3AOD.

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
    dev = pywpc.WifiDAQE3AOD()

    ## Connect to device
    try:
        dev.connect("192.168.5.38") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        filename = "WPC_test.txt"
        read_bytes = 15
        mode = 1 ## 0 : write, 1 : read

        ## Open file in sdcard
        err = await dev.SD_openFile_async(filename, mode)
        print(f"SD_openFile_async, status: {err}")

        ## Get sdcard storage
        storage = await dev.SD_getStorage_async()
        print(f"SD_getStorage_async: {storage}")

        ## Read data form sdcard
        read_data = await dev.SD_readFile_async(read_bytes)
        print(f"SD_readFile_async, data: {read_data}")

        ## Close file in sdcard
        err = await dev.SD_closeFile_async()
        print(f"SD_closeFile_async, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
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