'''
AI - AI_continuous_with_logger.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode with 8 channels from USBDAQF1AOD.
Then, save data into CSV file.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading and saving the streaming AI data.
Finally, it concludes by explaining how to close the AI.

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
        mode = 2 ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 200
        read_points = 200
        delay = 0.2 ## second

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open file with WPC_test.csv
        err = dev.Logger_openFile("WPC_test.csv")
        print(f"Logger_openFile: {err}")

        ## Write header into CSV file
        err = dev.Logger_writeHeader(["CH0","CH1","CH2","CH3","CH4","CH5","CH6","CH7"])
        print(f"Logger_writeHeader: {err}")

        ## Open port
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}: {err}")

        ## Set AI acquisition mode to continuous mode (2)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}: {err}")

        ## Set AI sampling rate
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in port {port}: {err}")

        ## Start AI
        err = await dev.AI_start_async(port)
        print(f"AI_start_async in port {port}: {err}")

        ## Wait for acquisition
        await asyncio.sleep(1) ## delay [s]

        ## Stop AI
        err = await dev.AI_stop_async(port)
        print(f"AI_stop_async in port {port}: {err}")

        data_len = 1
        while data_len > 0:
            ## Read data acquisition
            ai_2Dlist = await dev.AI_readStreaming_async(port, read_points, delay=delay)
            print(f"number of samples = {len(ai_2Dlist)}" )

            ## Write data into CSV file
            dev.Logger_write2DList(ai_2Dlist)

            ## Update data len
            data_len = len(ai_2Dlist)

        ## Close AI
        err = await dev.AI_close_async(port)
        print(f"AI_close_async in port {port}: {err}")
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