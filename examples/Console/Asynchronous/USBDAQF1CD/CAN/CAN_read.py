'''
CAN - CAN_read.py with asynchronous mode.

This example demonstrates how to read data from another device with CAN interface from USBDAQF1CD.

First, it shows how to open CAN port and configure CAN parameters.
Second, read bytes from another device.
Last, stop and close CAN port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
        port  = 1
        speed = 0 ## 0 = 125 KHz, 1 = 250 kHz, 2 = 500 kHz, 3 = 1 MHz
        read_delay = 0.005 ## second

        ## Get Firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open CAN
        err = await dev.CAN_open_async(port)
        print(f"CAN_open_async in port {port}: {err}")

        ## Set CAN port and set speed to 0
        err = await dev.CAN_setSpeed_async(port, speed)
        print(f"CAN_setSpeed_async in port {port}: {err}")

        ## Set CAN port and start CAN
        err = await dev.CAN_start_async(port)
        print(f"CAN_start_async in port {port}: {err}")

        ## Read 5 frames for 1000 times
        for i in range(1000):
            frame_list = await dev.CAN_read_async(port, 5, read_delay)
            if len(frame_list) > 0 :
                for frame in frame_list:
                    print(frame)
            else:
                ## Wait
                await asyncio.sleep(0.01) ## delay [s]

        ## Set CAN port and stop CAN
        err = await dev.CAN_stop_async(port)
        print(f"CAN_stop_async in port {port}: {err}")

        ## Close CAN
        err = await dev.CAN_close_async(port)
        print(f"CAN_close_async in port {port}: {err}")
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