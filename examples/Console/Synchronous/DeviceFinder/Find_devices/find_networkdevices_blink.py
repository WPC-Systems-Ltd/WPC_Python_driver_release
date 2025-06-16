'''
Find_devices - find_network_devices_blink.py with synchronous mode.

This example demonstrates how to find ethernet devices and blink.

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

    ## Perform network device information
    print("Find all network devices....")
    try:
        dev_2d_list = dev.Bcst_enumerateNetworkDevices()
        for device_list in dev_2d_list:
            print(device_list)
            mac_num = device_list[2]

            ## Check MAC and let LED blink
            err = dev.Bcst_checkMACAndRing(mac_num)
            print(f"Bcst_checkMACAndRing, status: {err}")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()