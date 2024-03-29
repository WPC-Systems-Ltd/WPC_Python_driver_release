'''
DIO - DO_blinky_pins.py with asynchronous mode.

This example illustrates the process of writing a high or low signal to a DO pin from EthanD.

To begin with, it demonstrates the steps required to open the DO pin.
Next, in each loop, a different voltage output is applied, resulting in a blinking effect.
Lastly, it concludes by closing the DO pin.

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
    dev = pywpc.EthanD()

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
        port = 0 ## Depend on your device
        pinindex = [1, 3, 5, 7]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pins with digital output
        err = await dev.DO_openPins_async(port, pinindex)
        print(f"DO_openPins_async in port {port}, status: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            state = await dev.DO_togglePins_async(port, pinindex)
            print(state)

            ## Wait for 0.5 second to see led status
            await asyncio.sleep(0.5)  ## delay [s]

        ## Close pins with digital output
        err = await dev.DO_closePins_async(port, pinindex)
        print(f"DO_closePins_async in port {port}, status: {err}")
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