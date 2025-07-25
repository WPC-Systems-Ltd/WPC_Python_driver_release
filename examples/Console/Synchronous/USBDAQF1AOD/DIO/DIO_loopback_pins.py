'''
DIO - DIO_loopback_pins.py with synchronous mode.

This example demonstrates the process of DIO loopback using pins from USBDAQF1AOD.
It involves using DO pins to send signals and DI pins to receive signals on a single device, commonly known as "loopback".

To begin with, it illustrates the steps required to open the DO and DI pins.
Next, it performs the operation of writing to a DO pin and reading from a DI pin.
Lastly, it concludes by closing the DO and DI pins.

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
    dev = pywpc.USBDAQF1AOD()

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
        timeout = 3  ## [sec]
        DO_port = 0  ## Depend on your device
        DI_port = 1
        DO_pins = [0, 1, 2, 3]
        DI_pins = [0, 1, 2, 3]
        DO_value = [1, 0, 1, 0]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open pins with digital output
        err = dev.DO_openPins(DO_port, DO_pins, timeout)
        print(f"DO_openPins in DO_port {DO_port}, status: {err}")

        ## Write pins to high or low
        err = dev.DO_writePins(DO_port, DO_pins, DO_value, timeout)
        print(f"DO_writePins in {DO_port}, status: {err}")

        ## Open pins with digital iutput
        err = dev.DI_openPins(DI_port, DI_pins, timeout)
        print(f"DI_openPins in DI_port {DI_port}, status: {err}")

        ## Read pins state
        state_list = dev.DI_readPins(DI_port, DI_pins, timeout)
        print(f"state_list in DI_port {DI_port}: {state_list}")

        ## Close pins with digital output
        err = dev.DO_closePins(DO_port, DO_pins, timeout)
        print(f"DO_closePins in DO_port {DO_port}, status: {err}")

        ## Close pins with digital input
        err = dev.DI_closePins(DI_port, DI_pins, timeout)
        print(f"DI_closePins in DI_port {DI_port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()