'''
Counter - Counter_read.py with synchronous mode.

This example demonstrates how to read counter with USBDAQF1DSNK.

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
    dev = pywpc.USBDAQF1DSNK()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        channel = 1  ## Depend on your device
        timeout = 3  ## [sec]
        edge = 0  ##  0: Falling edge, 1: Rising edge
        window_size = 100
        position = 0

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open counter
        err = dev.Counter_open(channel, timeout)
        print(f"Counter_open in channel {channel}, status: {err}")

        ## Set counter edge
        err = dev.Counter_setEdge(channel, edge, timeout)
        print(f"Counter_setEdge in channel {channel}, status: {err}")

        ## Set counter frequency window size
        err = dev.Counter_setFreqWindow(channel, window_size, timeout)
        print(f"Counter_setFreqWindow in channel {channel}, status: {err}")

        ## Set counter position
        err = dev.Counter_setPosition(channel, position, timeout)
        print(f"Counter_setPosition in channel {channel}, status: {err}")

        ## Start counter
        err = dev.Counter_start(channel, timeout)
        print(f"Counter_start in channel {channel}, status: {err}")

        ## Read counter position
        while True:
            posi = dev.Counter_readPosition(channel, timeout)
            print(f"Read counter position in channel {channel}: {posi}")
    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop counter
        err = dev.Counter_stop(channel, timeout)
        print(f"Counter_stop in channel {channel}, status: {err}")

        ## Close counter
        err = dev.Counter_close(channel, timeout)
        print(f"Counter_close in channel {channel}, status: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()