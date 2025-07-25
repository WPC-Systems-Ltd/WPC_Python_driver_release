'''
AI - AI_N_samples_once.py with synchronous mode.

This example demonstrates the process of obtaining AI data in N-sample mode.
Additionally, it gets AI data with points in once from USBDAQF1AOD.

To begin with, it demonstrates the steps to open the AI and configure the AI parameters.
Next, it outlines the procedure for reading the streaming AI data.
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


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        mode = 1  ## 0: On demand, 1: N-samples, 2: Continuous
        channel = 8
        sampling_rate = 1000
        samples = 200
        read_points = 200
        read_delay = 3  ## [sec]
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open AI
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port {port}, status: {err}")
        
        ## Set AI channel
        err = dev.AI_enableChannel(port, channel, timeout)
        print(f"AI_enableChannel in port {port}, status: {err}")

        ## Set AI acquisition mode to N-samples mode (1)
        err = dev.AI_setMode(port, mode, timeout)
        print(f"AI_setMode {mode} in port {port}, status: {err}")

        ## Set AI sampling rate
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout)
        print(f"AI_setSamplingRate {sampling_rate} in port {port}, status: {err}")

        ## Set AI # of samples
        err = dev.AI_setNumSamples(port, samples, timeout)
        print(f"AI_setNumSamples {samples} in port {port}, status: {err}")

        ## Open AI streaming
        err = dev.AI_openStreaming(port, timeout)
        print(f"AI_openStreaming in port {port}, status: {err}")

        ## Start AI streaming
        err = dev.AI_startStreaming(port, timeout)
        print(f"AI_startStreaming in port {port}, status: {err}")

        ## Read AI
        ai_2Dlist = dev.AI_readStreaming(port, read_points, read_delay)
        print(f"Number of samples: {len(ai_2Dlist)}")

        ok = True
        for i, ai_list in enumerate(ai_2Dlist):
            ## Check for any missing data
            if len(ai_list) != channel:
                print(i, ai_list)
                ok = False
        if ok:
            print('Sample length OK')
        else:
            print('Error: at least 1 sample has wrong length')

        ## Close AI streaming
        err = dev.AI_closeStreaming(port, timeout)
        print(f"AI_closeStreaming in port {port}, status: {err}")

        ## Close AI
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()