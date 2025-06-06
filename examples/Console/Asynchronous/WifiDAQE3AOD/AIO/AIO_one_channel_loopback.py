'''
AIO - AIO_one_channel_loopback.py with asynchronous mode.

This example demonstrates the process of AIO loopback with specific channels of WifiDAQE3AOD.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO.
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

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
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3AOD()

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
        port = 0 ## Depend on your device
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}, status: {err}")
        

        ## Open AO
        err = await dev.AO_open_async(port)
        print(f"AO_open_async in port {port}, status: {err}")

        ## Read data acquisition
        ai_list = await dev.AI_readOnDemand_async(port)
        print(f"AI data in port {port}: {ai_list}")

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

        ## Read data acquisition
        ai_list = await dev.AI_readOnDemand_async(port)
        print(f"AI data in port {port}: {ai_list}")

        ## Close AI
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}, status: {err}")

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