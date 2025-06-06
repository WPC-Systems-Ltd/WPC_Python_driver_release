'''
CAN - CAN_write.py with asynchronous mode.

This example demonstrates how to write data to another device with CAN interface from USBDAQF1CD.

First, it shows how to open CAN port and configure CAN parameters.
Second, write bytes to another device.
Last, stop and close CAN port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

    ## Connect to device
    try:
        dev.connect("default") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 1 ## Depend on your device
        speed = 0 ## 0 = 125 KHz, 1 = 250 kHz, 2 = 500 kHz, 3 = 1 MHz

        ## Get Firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open CAN
        err = await dev.CAN_open_async(port)
        print(f"CAN_open_async in port {port}, status: {err}")

        ## Set CAN port and set speed to 0
        err = await dev.CAN_setSpeed_async(port, speed)
        print(f"CAN_setSpeed_async in port {port}, status: {err}")

        ## Set CAN port and start CAN
        err = await dev.CAN_start_async(port)
        print(f"CAN_start_async in port {port}, status: {err}")

        ## CAN_length: True: Extended, False: Standard
        ## CAN_type:   True: Remote, False: Data

        ## ID: 10, data with 8 bytes, Standard & Data
        err = await dev.CAN_write_async(port, 10, [33, 22, 11, 88, 77, 55, 66, 22], False, False)
        print(f"CAN_write_async in port {port}, status: {err}")

        ## Wait for 1 sec
        await asyncio.sleep(1) ## delay [s]

        ## ID: 20, data less than 8 bytes, Standard & Data
        err = await dev.CAN_write_async(port, 20, [1, 2, 3], False, False)
        print(f"CAN_write_async in port {port}, status: {err}")

        ## Wait for 1 sec
        await asyncio.sleep(1) ## delay [s]

        ## Set CAN port and stop CAN
        err = await dev.CAN_stop_async(port)
        print(f"CAN_stop_async in port {port}, status: {err}")

        ## Close CAN
        err = await dev.CAN_close_async(port)
        print(f"CAN_close_async in port {port}, status: {err}")
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