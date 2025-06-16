'''
DIO - DO_blinky_port.py with asynchronous mode.

This example illustrates the process of writing a high or low signal to a DO port from STEM.

To begin with, it demonstrates the steps required to open the DO port.
Next, in each loop, a different voltage output is applied, resulting in a blinking effect.
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
    dev = pywpc.STEM()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        slot = 1  ## Connect DIO module to slot
        DO_port = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

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
        print(f"Enable: {info[0]}")
        print(f"Direction: {info[1]}")
        print(f"State: {info[2]}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            state = await dev.DO_togglePort_async(DO_port)
            print(state)

            ## Wait for 0.5 second to see led status
            await asyncio.sleep(0.5)   ## delay [sec]
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
