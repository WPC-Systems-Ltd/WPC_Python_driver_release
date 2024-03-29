'''
AO - AO_write_one_channel.py with asynchronous mode.

This example demonstrates the process of writing AO signal of USBDAQF1AOD.
To begin with, it demonstrates the steps to open AO.
Next, it outlines the procedure for writing digital signals with channel to the AO pins.
Finally, it concludes by explaining how to close AO.

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
    dev = pywpc.USBDAQF1AOD()

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
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AO
        err = await dev.AO_open_async(port)
        print(f"AO_open_async in port {port}, status: {err}")

        ## Write AO vaule in channel 0
        err = await dev.AO_writeOneChannel_async(port, 0, ao_value_list[0])
        print(f"In port {port} channel 0, the AO value is {ao_value_list[0]}, status: {err}")

        ## Write AO vaule in channel 1
        err = await dev.AO_writeOneChannel_async(port, 1, ao_value_list[1])
        print(f"In port {port} channel 1, the AO value is {ao_value_list[1]}, status: {err}")

        ## Write AO vaule in channel 2
        err = await dev.AO_writeOneChannel_async(port, 2, ao_value_list[2])
        print(f"In port {port} channel 2, the AO value is {ao_value_list[2]}, status: {err}")

        ## Write AO vaule in channel 3
        err = await dev.AO_writeOneChannel_async(port, 3, ao_value_list[3])
        print(f"In port {port} channel 3, the AO value is {ao_value_list[3]}, status: {err}")

        ## Close AO
        err = await dev.AO_close_async(port)
        print(f"AO_close_async in port {port}, status: {err}")
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