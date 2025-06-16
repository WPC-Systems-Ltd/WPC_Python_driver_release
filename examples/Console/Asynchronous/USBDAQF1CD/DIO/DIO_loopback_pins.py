'''
DIO - DIO_loopback_pins.py with asynchronous mode.

This example demonstrates the process of DIO loopback using pins from USBDAQF1CD.
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

## Python
import asyncio
import sys
sys.path.insert(0, 'src/')


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

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
        DO_port = 0  ## Depend on your device
        DI_port = 1
        DO_pins = [0, 1, 2, 3]
        DI_pins = [0, 1, 2, 3]
        DO_value = [1, 0, 1, 0]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open pins with digital output
        err = await dev.DO_openPins_async(DO_port, DO_pins)
        print(f"DO_openPins_async in DO_port {DO_port}, status: {err}")

        ## Write pins to high or low
        err = await dev.DO_writePins_async(DO_port, DO_pins, DO_value)
        print(f"DO_writePins_async in DO_port {DO_port}, status: {err}")

        ## Open pins with digital iutput
        err = await dev.DI_openPins_async(DI_port, DI_pins)
        print(f"DI_openPins_async in DI_port {DI_port}, status: {err}")

        ## Read pins state
        state_list = await dev.DI_readPins_async(DI_port, DI_pins)
        print(state_list)

        ## Close pins with digital output
        err = await dev.DO_closePins_async(DO_port, DO_pins)
        print(f"DO_closePins_async in DO_port {DO_port}, status: {err}")

        ## Close pins with digital input
        err = await dev.DI_closePins_async(DI_port, DI_pins)
        print(f"DI_closePins_async in DI_port {DI_port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
