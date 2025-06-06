'''
AIO - AIO_all_channels_loopback.py with synchronous mode.

This example demonstrates the process of AIO loopback across all channels of USBDAQF1AOD.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO.
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

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
        ao_value_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        timeout = 3 ## second
        channel = 8

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AI
        err = dev.AI_open(port, timeout)
        print(f"AI_open in port {port}, status: {err}")
        

        ## Set AI channel
        err = dev.AI_enableChannel(port, channel, timeout)
        print(f"AI_enableChannel in port {port}, status: {err}")

        ## Open AO
        err = dev.AO_open(port, timeout)
        print(f"AO_open in port {port}, status: {err}")

        ## Read data acquisition
        ai_list = dev.AI_readOnDemand(port, timeout)
        print(f"AI data in port {port}: {ai_list}")

        ## Write AO value simultaneously
        err = dev.AO_writeAllChannels(port, ao_value_list, timeout)
        print(f"In port {port} the AO value is {ao_value_list}, status: {err}")

        ## Read data acquisition
        ai_list = dev.AI_readOnDemand(port, timeout)
        print(f"AI data in port {port}: {ai_list}")

        ## Close AI
        err = dev.AI_close(port, timeout)
        print(f"AI_close in port {port}, status: {err}")

        ## Close AO
        err = dev.AO_close(port, timeout)
        print(f"AO_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()