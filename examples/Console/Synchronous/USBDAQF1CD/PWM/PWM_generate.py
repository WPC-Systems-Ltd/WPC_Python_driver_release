'''
PWM - PWM_generate.py with synchronous mode.

This example demonstrates how to generate PWM with USBDAQF1CD.

First, you should set frequency and duty cycle so that it can generate proper signal.
By the way, if you want to check PWM signal, you could connect DI pin with PWM pin.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

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
        channel = 0 ## Depend on your device
        frequency = 100
        duty_cycle = 50
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open PWM
        err = dev.PWM_open(channel, timeout)
        print(f"PWM_open in channel {channel}, status: {err}")

        ## Set frequency
        err = dev.PWM_setFrequency(channel, frequency, timeout)
        print(f"PWM_setFrequency in channel {channel}, status: {err}")

        ## Set duty cycle
        err = dev.PWM_setDutyCycle(channel, duty_cycle, timeout)
        print(f"PWM_setDutyCycle in channel {channel}, status: {err}")

        ## Start PWM
        err = dev.PWM_start(channel, timeout)
        print(f"PWM_start in channel {channel}, status: {err}")

        ## Wait for seconds for generating signal
        time.sleep(5) ## delay [s]

        ## Stop PWM
        err = dev.PWM_stop(channel, timeout)
        print(f"PWM_stop in channel {channel}, status: {err}")

        ## Close PWM
        err = dev.PWM_close(channel, timeout)
        print(f"PWM_close in channel {channel}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()