'''
AI - AI_continuous.py with synchronous mode.

This example demonstrates the process of obtaining AI data in continuous mode.
Additionally, it utilizes a loop to retrieve AI data with 8 channels from WifiDAQE3A with a timeout of 100 ms.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
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


def loop_func(handle, port, get_samples=600, delay=0.05, exit_time=3):
    time_cal = 0
    while time_cal < exit_time:
        ## Read data acquisition
        data = handle.AI_readStreaming(port, get_samples, delay=delay)

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
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.35") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        mode = 2 ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = dev.AI_open(port, timeout=timeout)
        print(f"AI_open in port {port}: {err}")

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
        get_samples = 200
        delay = 0.05
        exit_time = 0.1

        ## Start loop
        loop_func(dev, port, get_samples, delay, exit_time)

        ## Stop AI
        err = dev.AI_stop(port, timeout=timeout)
        print(f"AI_stop in port {port}: {err}")

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