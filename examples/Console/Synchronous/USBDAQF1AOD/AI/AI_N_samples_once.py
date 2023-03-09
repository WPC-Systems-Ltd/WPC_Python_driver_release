'''
AI - AI_N_samples_once.py with synchronous mode.

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from USBDAQF1AOD.

First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
Last, close AI port.

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
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50
        read_points = 50
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open port
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port{port}: {err}")

        ## Set AI port and acquisition mode to N-samples mode (1)
        err = dev.AI_setMode(port, mode, timeout)
        print(f"AI_setMode in port{port}: {err}")

        ## Set AI port and sampling rate to 1k (Hz)
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout)
        print(f"AI_setSamplingRate in port{port}: {err}")

        ## Set AI port and # of samples to 50 (pts)
        err = dev.AI_setNumSamples(port, samples, timeout)
        print(f"AI_setNumSamples in port{port}: {err}")

        ## Set AI port and start acquisition
        err = dev.AI_start(port, timeout)
        print(f"AI_start in port{port}: {err}")

        ## Wait 1 seconds for acquisition
        time.sleep(1) ## delay [s]

        ## Set AI port and get 50 points
        data = dev.AI_readStreaming(port, read_points)

        ## Read acquisition data 50 points
        print("Get data points: " + str(len(data)))
        print("Get data: " + str(data))

        ## Close port
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port{port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()