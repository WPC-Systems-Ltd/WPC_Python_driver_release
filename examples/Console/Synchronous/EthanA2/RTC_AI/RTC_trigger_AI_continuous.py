
'''
RTC_AI - RTC_trigger_AI_continuous.py with synchronous mode.

This example demonstrates how to use RTC to trigger AI with continuous mode from EthanA2.

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
    dev = pywpc.EthanA2()

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
        mode = 2 ## 1 : N-samples, 2 : Continuous
        trigger_mode = 1 ## 1 : Use RTC to start AI streaming
        sampling_rate = 1000
        read_points = 200
        read_delay = 0.5 ## second
        timeout = 3 ## second
        mode_alarm = 0
        year = 2024
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

        ## Set AI trigger mode
        err = dev.AI_setTriggerMode(port, trigger_mode, timeout)
        print(f"AI_setTriggerMode {trigger_mode} in port {port}, status: {err}")

        ## Set AI sampling rate
        err = dev.AI_setSamplingRate(port, sampling_rate, timeout)
        print(f"AI_setSamplingRate {sampling_rate} in port {port}, status: {err}")

        ## Set RTC
        err = dev.Sys_setRTC(year, month, day, hour, minute, second-10, timeout)
        print(f"Set RTC to {year}-{month}-{day}, {hour}:{minute}:{second-10}, status: {err}")

        ## Open AI streaming
        err = dev.AI_openStreaming(port, timeout)
        print(f"AI_openStreaming in port {port}, status: {err}")

        ## Start RTC alarm after 10 seconds
        err = dev.Sys_startRTCAlarm(mode_alarm, day, hour, minute, second, timeout)
        print(f"Alarm RTC to {year}-{month}-{day}, {hour}:{minute}:{second}, status: {err}")

        stop_flag = 1
        for i in range(15):
            ## Read data acquisition
            ai_2Dlist = dev.AI_readStreaming(port, read_points, read_delay)
            print(f"len: {len(ai_2Dlist)}, {dev.Sys_getRTC()}" )
            if len(ai_2Dlist)> 0 and stop_flag == 1 :
                ## Close AI streaming
                err = dev.AI_closeStreaming(port, timeout)
                print(f"AI_closeStreaming in port {port}, status: {err}")
                stop_flag = 0
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