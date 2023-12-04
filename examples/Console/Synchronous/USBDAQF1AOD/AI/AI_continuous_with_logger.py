'''
AI - AI_continuous_with_logger.py with synchronous mode.

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
import time

## WPC

from wpcsys import pywpc


def main():
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
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open file with WPC_test.csv
        err = dev.Logger_openFile("WPC_test.csv")
        print(f"Logger_openFile: {err}")

        ## Write header into CSV file
        err = dev.Logger_writeHeader(["CH0","CH1","CH2","CH3","CH4","CH5","CH6","CH7"])
        print(f"Logger_writeHeader: {err}")

        ## Open AI
        err = dev.AI_open(port, timeout=timeout)
        print(f"AI_open in port {port}: {err}")

        ## Set AI acquisition mode to continuous mode (2)
        err = dev.AI_setMode(port, mode, timeout=timeout)
        print(f"AI_setMode {mode} in port {port}: {err}")

        ## Set AI sampling rate
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout=timeout)
        print(f"AI_setSamplingRate {sampling_rate} in port {port}: {err}")

        ## Start AI
        err = dev.AI_start(port, timeout=timeout)
        print(f"AI_start in port {port}: {err}")

        ## Wait a while for data acquisition
        time.sleep(1) ## delay [s]

        ## Stop AI
        err = dev.AI_stop(port, timeout=timeout)
        print(f"AI_stop in port {port}: {err}")

        data_len = 1
        while data_len > 0:
            ## Read data acquisition
            ai_2Dlist = dev.AI_readStreaming(port, read_points, delay=delay)
            print(f"number of samples = {len(ai_2Dlist)}" )

            ## Write data into CSV file
            dev.Logger_write2DList(ai_2Dlist)

            ## Update data len
            data_len = len(ai_2Dlist)

        ## Close AI
        err = dev.AI_close(port, timeout=timeout)
        print(f"AI_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()