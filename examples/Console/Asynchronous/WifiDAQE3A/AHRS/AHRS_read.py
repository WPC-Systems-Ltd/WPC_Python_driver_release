'''
AHRS - AHRS_read.py with asynchronous mode.

This example demonstrates the process of obtaining AHRS three axis estimation data.

To begin with, it demonstrates the steps to open the AHRS and configure the AHRS parameters.
Next, it outlines the procedure for reading the streaming AHRS data.
Finally, it concludes by explaining how to close the AHRS.

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
    dev = pywpc.WifiDAQE3A()

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
        sampling_period = 0.003
        read_delay = 0.05 ## second

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = await dev.AHRS_open_async(port)
        print(f"AHRS_open_async in port {port}: {err}")

        ## Set period
        err = await dev.AHRS_setSamplingPeriod_async(port, sampling_period)
        print(f"AHRS_setSamplingPeriod_async in port {port}: {err}")

        ## Start AHRS
        err = await dev.AHRS_start_async(port)
        print(f"AHRS_start_async in port {port}: {err}")

        ## Wait for acquisition
        await asyncio.sleep(1) ## delay [s]

        ## Read AHRS estimation
        for i in range(10):
            ahrs_list = await dev.AHRS_readStreaming_async(port, read_delay)
            print(f"Roll: {ahrs_list[0]}, Pitch: {ahrs_list[1]}, Yaw: {ahrs_list[2]}")

        ## Stop AHRS
        err = await dev.AHRS_stop_async(port)
        print(f"AHRS_stop_async in port {port}: {err}")

        ## Close AHRS
        err = await dev.AHRS_close_async(port)
        print(f"AHRS_close_async in port {port}: {err}")
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