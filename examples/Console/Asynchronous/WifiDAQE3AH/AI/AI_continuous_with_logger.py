'''
AI - AI_continuous_with_logger.py with asynchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode with 8 channels from WifiDAQE3AH.
Then, save data into CSV file.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading and saving the streaming AI data.
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
    dev = pywpc.WifiDAQE3AH()

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
        mode = 2  ## 0: On demand, 1: N-samples, 2: Continuous
        sampling_rate = 200
        read_points = 200
        read_delay = 0.2  ## [sec]
        

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")
        ## Open file with WPC_test.csv
        err = dev.Logger_openFile("WPC_test.csv")
        print(f"Logger_openFile, status: {err}")

        ## Write header into CSV file
        err = dev.Logger_writeHeader(["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"])
        print(f"Logger_writeHeader, status: {err}")

        ## Open AI
        err = await dev.AI_open_async(port)
        print(f"AI_open_async in port {port}, status: {err}")
        

        ## Set AI acquisition mode to continuous mode (2)
        err = await dev.AI_setMode_async(port, mode)
        print(f"AI_setMode_async {mode} in port {port}, status: {err}")

        ## Set AI sampling rate
        err = await dev.AI_setSamplingRate_async(port, sampling_rate)
        print(f"AI_setSamplingRate_async {sampling_rate} in port {port}, status: {err}")

        ## Open AI streaming
        err = await dev.AI_openStreaming_async(port)
        print(f"AI_openStreaming_async in port {port}, status: {err}")

        ## Start AI streaming
        err = await dev.AI_startStreaming_async(port)
        print(f"AI_startStreaming_async in port {port}, status: {err}")

        ## Wait for acquisition
        await asyncio.sleep(1)  ## delay [sec]

        ## Close AI streaming
        err = await dev.AI_closeStreaming_async(port)
        print(f"AI_closeStreaming_async in port {port}, status: {err}")

        data_len = 1
        while data_len > 0:
            ## Read data acquisition
            ai_2Dlist = await dev.AI_readStreaming_async(port, read_points, read_delay)
            print(f"number of samples = {len(ai_2Dlist)}")

            ## Write data into CSV file
            dev.Logger_write2DList(ai_2Dlist)

            ## Update data len
            data_len = len(ai_2Dlist)

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
