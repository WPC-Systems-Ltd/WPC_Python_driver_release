'''
DIO - DIO_loopback_port.py with asynchronous mode.

This example demonstrates the process of DIO loopback using port from USBDAQF1DSNK.
It involves using DO port to send signals and DI port to receive signals on a single device, commonly known as "loopback".

To begin with, it illustrates the steps required to open the DO and DI port.
Next, it performs the operation of writing to a DO pin and reading from a DI pin.
Lastly, it concludes by closing the DO and DI port.

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
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1DSNK()

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
        port = 0 ## Depend on your device
        DO_port = 0
        DI_port = 1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode:", port_mode)

        ## If the port mode is not set to "DIO", set the port mode to "DIO"
        if port_mode != "DIO":
            err = await dev.Sys_setPortDIOMode_async(port)
            print(f"Sys_setPortDIOMode_async in port {port}: {err}")

        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode:", port_mode)

        ## Get port DIO start up information
        info = await dev.DIO_loadStartup_async(DO_port)
        print("Enable:   ", info[0])
        print("Direction:", info[1])
        print("State:    ", info[2])

        ## Write DO port to high or low
        err = await dev.DO_writePort_async(DO_port, [1, 0, 1, 0])
        print(f"DO_writePort_async in port {DO_port}: {err}")

        ## Read DI port state
        state_list = await dev.DI_readPort_async(DI_port)
        print(f"state_list in port {DI_port}: {state_list}")

        
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