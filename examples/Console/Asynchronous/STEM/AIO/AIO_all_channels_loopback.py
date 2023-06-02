'''
AIO - AIO_all_channels_loopback.py with asynchronous mode.

This example demonstrates the process of AIO loopback across all channels of STEM.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO port
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

If your product is "STEM", please invoke the function `Sys_setPortAIOMode_async` and `AI_enableCS_async`.
Example: AI_enableCS_async is {0, 2}
Subsequently, the returned value of AI_readOnDemand_async and AI_readStreaming_async will be displayed as follows.
data:
          CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH0, CH1, CH2, CH3, CH4, CH5, CH6, CH7
          |                                     |                                      |
          |---------------- CS0-----------------|---------------- CS2------------------|
[sample0]
[sample1]
   .
   .
   .
[sampleN]

--------------------------------------------------------------------------------------
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
        print("Slot mode:", port_mode)

        ## If the port mode is not set to "AIO", set the port mode to "AIO"
        if port_mode != "AIO":
            err = await dev.Sys_setPortAIOMode_async(port)
            print(f"Sys_setPortAIOMode_async in port {port}: {err}")

        ## Get port mode
        port_mode = await dev.Sys_getPortMode_async(port)
        print("Slot mode:", port_mode)

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

        ## Set AO port and write data simultaneously
        ## CH0~CH1 5V, CH2~CH3 3V, CH4~CH5 2V, CH6~CH7 0V
        err = await dev.AO_writeAllChannels_async(port, [5,5,3,3,2,2,0,0])
        print(f"AO_writeAllChannels_async in port {port}: {err}")

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