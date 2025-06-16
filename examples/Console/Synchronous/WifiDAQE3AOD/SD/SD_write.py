'''
SD - SD_write.py with synchronous mode.

This example demonstrates how to write a message in SD card from WifiDAQE3AOD.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AOD()

    ## Connect to device
    try:
        dev.connect("192.168.5.38")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        filename = "WPC_test.txt"
        write_data = "12345"
        mode = 0  ## 0 : write, 1 : read
        timeout = 3  ## [sec]

        ## Open file in sdcard
        err = dev.SD_openFile(filename, mode, timeout)
        print(f"SD_openFile, status: {err}")

        ## Get sdcard storage
        storage = dev.SD_getStorage(timeout)
        print(f"SD_getStorage: {storage}")

        ## Write data in sdcard
        err = dev.SD_writeFile(write_data, timeout)
        print(f"SD_writeFile, status: {err}")

        ## Close file in sdcard
        err = dev.SD_closeFile(timeout)
        print(f"SD_closeFile, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()


if __name__ == '__main__':
    main()