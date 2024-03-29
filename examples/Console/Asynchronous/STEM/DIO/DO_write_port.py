'''
DIO - DO_write_port.py with asynchronous mode.

This example illustrates the process of writing a high or low signal to a DO port from STEM.

To begin with, it demonstrates the steps required to open the DO port.
Next, voltage output is written to the DO port.
Lastly, it concludes by closing the DO port.

If your product is "STEM", please invoke the function `Sys_setDIOMode_async`.

The DIO ports 0 to 1 are assigned to slot 1, while ports 2 to 3 are assigned to slot 2.
---------------------------
|  Slot 1    port 1 & 0   |
|  Slot 2    port 3 & 2   |
|  Slot 3    port 5 & 4   |
|  Slot 4    port 7 & 6   |
---------------------------

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
    dev = pywpc.STEM()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        slot = 1 ## Connect DIO module to slot
        DO_port = 0
        DO_value = [1, 0, 1, 0]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Get slot mode
        slot_mode = await dev.Sys_getMode_async(slot)
        print("Slot mode:", slot_mode)

        ## If the slot mode is not set to "DIO", set the slot mode to "DIO"
        if slot_mode != "DIO":
            err = await dev.Sys_setDIOMode_async(slot)
            print(f"Sys_setDIOMode_async in slot {slot}, status: {err}")

        ## Get slot mode
        slot_mode = await dev.Sys_getMode_async(slot)
        print("Slot mode:", slot_mode)

        ## Get DIO start up information
        info = await dev.DIO_loadStartup_async(DO_port)
        print("Enable:   ", info[0])
        print("Direction:", info[1])
        print("State:    ", info[2])

        ## Write port to high or low
        err = await dev.DO_writePort_async(DO_port, DO_value)
        print(f"DO_writePort_async in port {DO_port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
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