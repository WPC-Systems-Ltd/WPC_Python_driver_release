'''
AI - AI_continuous_with_logger.py with synchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode and saving it into a CSV file.
Additionally, it utilizes a loop to retrieve AI data with 8 channels from STEM with a timeout of 100 ms.

To begin with, it demonstrates the steps to open the AI port and configure the AI parameters.
Next, it outlines the procedure for reading and saving the streaming AI data.
Finally, it concludes by explaining how to close the AI port.

If your product is "STEM", please invoke the function `Sys_setPortAIOMode`and `AI_enableCS`.
Example: AI_enableCS is {0, 2}
Subsequently, the returned value of AI_readOnDemand and AI_readStreaming will be displayed as follows.
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

def loop_func(handle, port, num_of_samples=600, delay=0.05, exit_loop_time=3):
    time_cal = 0
    while time_cal < exit_loop_time:
        ## Read data acquisition
        data = handle.AI_readStreaming(port, num_of_samples, delay=delay) ## Get 600 points at a time

        ## Write data into CSV file
        handle.Logger_write2DList(data)

        ## Print data
        for i in range(len(data)):
            print(f"{data[i]}")

        ## Wait
        time.sleep(delay) ## delay [s]
        time_cal += delay

def main():
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
        mode = 2  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        timeout = 3  ## second
        chip_select = [0, 1]

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
        
        ## Get port mode
        port_mode = dev.Sys_getPortMode(port, timeout=timeout)
        print("Slot mode:", port_mode)

        ## If the port mode is not set to "AIO", set the port mode to "AIO"
        if port_mode != "AIO":
            err = dev.Sys_setPortAIOMode(port, timeout=timeout)
            print(f"Sys_setPortAIOMode in port {port}: {err}")

        ## Get port mode
        port_mode = dev.Sys_getPortMode(port, timeout=timeout)
        print("Slot mode:", port_mode)

        ## Open port
        err = dev.AI_open(port, timeout=timeout)
        print(f"AI_open in port {port}: {err}")

        ## Enable CS
        err = dev.AI_enableCS(port, chip_select, timeout=timeout)
        print(f"AI_enableCS in port {port}: {err}")
        
        ## Set AI acquisition mode to continuous mode (2)
        err = dev.AI_setMode(port, mode, timeout=timeout)
        print(f"AI_setMode {mode} in port {port}: {err}")

        ## Set AI sampling rate to 1k (Hz)
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout=timeout)
        print(f"AI_setSamplingRate {sampling_rate} in port {port}: {err}")

        ## Start AI acquisition
        err = dev.AI_start(port, timeout=timeout)
        print(f"AI_start in port {port}: {err}")

        ## Set loop parameters
        num_of_samples = 200
        delay = 0.05
        exit_loop_time = 0.1

        ## Start loop
        loop_func(dev, port, num_of_samples=num_of_samples, delay=delay, exit_loop_time=exit_loop_time)

        ## Close port
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