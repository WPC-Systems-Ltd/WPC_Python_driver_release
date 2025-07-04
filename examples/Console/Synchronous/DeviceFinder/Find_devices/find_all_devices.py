'''
Find_devices - find_all_devices.py with synchronous mode.

This example demonstrates how to find all available USB and ethernet devices.

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
    dev = pywpc.DeviceFinder()

    ## Connect to device
    dev.connect()

    ## Perform USB device information
    print("Find all USB devices....")
    try:
        dev_2d_list = dev.Bcst_enumerateUSBDevices()
        for device_list in dev_2d_list:
            print(device_list)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform network device information
    print("Find all network devices....")
    try:
        dev_2d_list = dev.Bcst_enumerateNetworkDevices()
        for device_list in dev_2d_list:
            print(device_list)
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()