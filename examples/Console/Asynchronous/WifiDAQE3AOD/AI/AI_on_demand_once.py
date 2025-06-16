'''
AI - AI_on_demand_once.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in on demand mode.
Additionally, it retrieve AI data from WifiDAQE3AOD.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the AI on demand data.
Finally, it concludes by explaining how to close the AI.

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
    dev = pywpc.WifiDAQE3AOD()

    ## Connect to device
    try:
        dev.connect("192.168.5.38")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        mode = 0
        

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open AI
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}, status: {err}")
        

        ## Set AI acquisition mode to on demand mode (0)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}, status: {err}")

        ## Read AI
        ai_list = await dev.AI_readOnDemand_async(port)
        print(f"data in port {port}: {ai_list}")

        ## Close AI
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}, status: {err}")
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
