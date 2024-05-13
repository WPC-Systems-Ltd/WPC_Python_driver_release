
'''
RTC_AI - RTC_trigger_AI_N_samples.py with synchronous mode.

This example demonstrates how to use RTC to trigger AI with N-samples mode from EthanA.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''
## WPC

from wpcsys import pywpc
import time

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanA()

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
        port = 0 ## Depend on your device
        mode = 4 ## 3 : RTC On demand, 4 : RTC N-samples, 5 : RTC Continuous
        sampling_rate = 1000
        samples = 200
        read_points = 200
        read_delay = 0.5 ## second
        timeout = 3 ## second
        mode_alarm = 0
        month = 4
        day = 2
        hour = 15
        minute = 8
        second = 50

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port {port}, status: {err}")

        ## Set AI mode
        err = dev.AI_setMode(port, mode, timeout)
        print(f"AI_setMode {mode} in port {port}, status: {err}")

        ## Set AI sampling rate
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout)
        print(f"AI_setSamplingRate {sampling_rate} in port {port}, status: {err}")

        ## Set AI # of samples
        err = dev.AI_setNumSamples(port, samples, timeout)
        print(f"AI_setNumSamples {samples} in port {port}, status: {err}")

        ## Set RTC
        err = dev.Sys_setRTC(2024, month, day, hour, minute, second-10, timeout)
        print(f"Set RTC to 2024-{month}-{day}, {hour}:{minute}:{second-10} , status: {err}")

        ## Start RTC alarm after 10 seconds
        err = dev.Sys_startRTCAlarm(mode_alarm, day, hour, minute, second, timeout)
        print(f"Alarm RTC to 2024-{month}-{day}, {hour}:{minute}:{second} , status: {err}")

        for i in range(10):
            ## Read data acquisition
            ai_2Dlist = dev.AI_readStreaming(port, read_points, read_delay)
            print(f"len: {len(ai_2Dlist)}, {dev.Sys_getRTC()}" )
            time.sleep(1)

        ## Close AI
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return
if __name__ == '__main__':
    main()