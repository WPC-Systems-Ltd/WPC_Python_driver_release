'''
AIO - AIO_one_channel_loopback.py with asynchronous mode.

This example demonstrates how to write AIO loopback in specific channel from STEM.
Use AO pins to send signals and use AI pins to receive signals on single device also called "loopback".

First, it shows how to open AO and AI in port.
Second, write digital signals to AO in specific channel and read AI ondemand data.
Last, close AO and AI in port.

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
        port = 1 ## Depend on your device
        chip_select = [0]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        
        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode: ", port_mode)

        if port_mode != "AIO":
            ## Set port to AIO mode
            err = await dev.Sys_setPortAIOMode_async(port)
            print(f"Sys_setPortAIOMode_async in port {port}: {err}")

        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode: ", port_mode)

        ## Open port
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}: {err}")

        ## Enable CS
        err = await dev.AI_enableCS_async(port, chip_select)
        print(f"AI_enableCS_async in port {port}: {err}")
        

        ## Open AO
        err = await dev.AO_open_async(port)
        print(f"AO_open_async in port {port}: {err}")

        ## Set AI port and data acquisition
        data = await dev.AI_readOnDemand_async(port)
        print(f"AI data in port {port}: {data}")

        ## Set AO port and write data 1.5(V) in channel 0
        err = await dev.AO_writeOneChannel_async(port, 0, 1.5)
        print(f"AO_writeOneChannel_async in ch0 in port {port}: {err}")

        ## Set AO port and write data 2.5(V) in channel 1
        err = await dev.AO_writeOneChannel_async(port, 1, 2.5)
        print(f"AO_writeOneChannel_async in ch1 in port {port}: {err}")

        ## Set AO port and write data 3.5(V) in channel 2
        err = await dev.AO_writeOneChannel_async(port, 2, 3.5)
        print(f"AO_writeOneChannel_async in ch2 in port {port}: {err}")

        ## Set AO port and write data 4.5(V) in channel 3
        err = await dev.AO_writeOneChannel_async(port, 3, 4.5)
        print(f"AO_writeOneChannel_async in ch3 in port {port}: {err}")

        ## Set AI port and data acquisition
        data = await dev.AI_readOnDemand_async(port)
        print(f"AI data in port {port}: {data}")

        ## Close AI
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}: {err}")

        ## Close AO
        err = await dev.AO_close_async(port)
        print(f"AO_close_async in port {port}: {err}")
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