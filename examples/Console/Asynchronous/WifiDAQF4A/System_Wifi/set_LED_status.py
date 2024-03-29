'''
System_Wifi - set_LED_status.py with asynchronous mode.

This example demonstrates how to set LED status from WifiDAQF4A.

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
    dev = pywpc.WifiDAQF4A()

    ## Connect to device
    try:
        dev.connect("192.168.5.38") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        value = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        for i in range(3):
            ## Reset LED status
            err = await dev.Wifi_resetLED_async()
            print(f"Wifi_resetLED_async, status: {err}")

            ## Set green LED status
            err = await dev.Wifi_setGreenLED_async(value)
            print(f"Wifi_setGreenLED_async, status: {err}")
            await asyncio.sleep(1) ## delay [s]

            ## Reset LED status
            err = await dev.Wifi_resetLED_async()
            print(f"Wifi_resetLED_async, status: {err}")

            ## Set blue LED status
            err = await dev.Wifi_setBlueLED_async(value)
            print(f"Wifi_setBlueLED_async, status: {err}")
            await asyncio.sleep(1) ## delay [s]

            ## Reset LED status
            err = await dev.Wifi_resetLED_async()
            print(f"Wifi_resetLED_async, status: {err}")

            ## Set red LED status
            err = await dev.Wifi_setRedLED_async(value)
            print(f"Wifi_setRedLED_async, status: {err}")
            await asyncio.sleep(1) ## delay [s]

            print("")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
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