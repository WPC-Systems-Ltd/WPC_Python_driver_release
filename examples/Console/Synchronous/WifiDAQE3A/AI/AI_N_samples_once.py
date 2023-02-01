'''
AI - AI_N_samples_once.py

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from WifiDAQE3A.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
Last, close AI port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python

import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50
        read_points = 50

        ## Open port
        err = dev.AI_open(port)
        print("AI_open:", err)

        ## Set AI port and acquisition mode to N-samples mode (1)
        err = dev.AI_setMode(port, mode)
        print("AI_setMode:", err)

        ## Set AI port and sampling rate to 1k (Hz)
        err = dev.AI_setSamplingRate(port, sampling_rate)
        print("AI_setSamplingRate:", err)

        ## Set AI port and # of samples to 50 (pts)
        err = dev.AI_setNumSamples(port, samples)
        print("AI_setNumSamples:", err)

        ## Set AI port and start acquisition
        err = dev.AI_start(port)
        print("AI_start:", err)

        ## Set AI port and get 50 points
        data = dev.AI_readStreaming(port, read_points)

        ## Read acquisition data 50 points
        print("Get data points:" + str(len(data)))
        print("Get data:" + str(data))

        ## Close port
        err = dev.AI_close(port)
        print("AI_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return
if __name__ == '__main__':
    main()