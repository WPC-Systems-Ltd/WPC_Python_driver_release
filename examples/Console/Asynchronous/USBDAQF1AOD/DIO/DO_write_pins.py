'''
DIO - DO_write_pins.py with asynchronous mode.

This example illustrates the process of writing a high or low signal to a DO pin from USBDAQF1AOD.

To begin with, it demonstrates the steps required to open the DO pin.
Next, voltage output is written to the DO pin.
Lastly, it concludes by closing the DO pin.

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
        port = 0  ## Depend on your device
        pin_index = [0, 1, 2, 3]
        DO_value = [1, 0, 1, 0]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open pins with digital output
        err = await dev.DO_openPins_async(port, pin_index)
        print(f"DO_openPins_async in port {port}, status: {err}")

        ## Write pins to high or low
        err = await dev.DO_writePins_async(port, pin_index, DO_value)
        print(f"DO_writePins_async in port {port}, status: {err}")

        ## Wait for seconds to see led status
        await asyncio.sleep(3)  ## delay [sec]

        ## Close pins with digital output
        err = await dev.DO_closePins_async(port, pin_index)
        print(f"DO_closePins_async in port {port}, status: {err}")

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
