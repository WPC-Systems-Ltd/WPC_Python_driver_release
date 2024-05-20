'''
SD - SD_write.py with synchronous mode.

This example demonstrates how to read a message from SD card from WifiDAQE3AH.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AH()

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
        read_bytes = 5
        mode = 1 ## 0 : write, 1 : read
        timeout = 3 ## second

        ## Open file in sdcard
        err = dev.SD_openFile(filename, mode, timeout)
        print(f"SD_openFile, status: {err}")

        ## Get sdcard storage
        storage = dev.SD_getStorage(timeout)
        print(f"SD_getStorage: {storage}")

        ## Read data form sdcard
        read_data = dev.SD_readFile(read_bytes, timeout)
        print(f"SD_readFile, data: {read_data}")

        ## Close file in sdcard
        err = dev.SD_closeFile(timeout)
        print(f"SD_closeFile, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()