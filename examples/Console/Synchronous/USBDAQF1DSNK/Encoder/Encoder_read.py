'''
Encoder - Encoder_read.py with synchronous mode.

This example demonstrates how to read encoder with USBDAQF1DSNK.

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
        channel = 0  ## Depend on your device
        timeout = 3  ## [sec]
        position = 0
        direction = 1  ## 1 : Forward, -1 : Reverse
        window_size = 100

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open encoder
        err = dev.Encoder_open(channel, timeout)
        print(f"Encoder_open in channel {channel}, status: {err}")

        ## Set encoder direction
        err = dev.Encoder_setDirection(channel, direction, timeout)
        print(f"Encoder_setDirection in channel {channel}, status: {err}")

        ## Set encoder position
        err = dev.Encoder_setPosition(channel, position, timeout)
        print(f"Encoder_setPosition in channel {channel}, status: {err}")

        ## Set encoder frequency window size
        err = dev.Encoder_setFreqWindow(channel, window_size, timeout)
        print(f"Encoder_setFreqWindow in channel {channel}, status: {err}")

        ## Start encoder
        err = dev.Encoder_start(channel, timeout)
        print(f"Encoder_start in channel {channel}, status: {err}")

        ## Read encoder position
        while True:
            position = dev.Encoder_readPosition(channel, timeout)
            print(f"Encoder position in channel {channel}: {position}")
    except KeyboardInterrupt:
        print("Press keyboard")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Stop encoder
        err = dev.Encoder_stop(channel, timeout)
        print(f"Encoder_stop in channel {channel}, status: {err}")

        ## Close encoder
        err = dev.Encoder_close(channel, timeout)
        print(f"Encoder_close in channel {channel}, status: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()