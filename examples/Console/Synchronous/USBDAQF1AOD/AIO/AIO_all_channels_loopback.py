'''
AIO - AIO_all_channels_loopback.py with synchronous mode.

This example demonstrates the process of AIO loopback across all channels of USBDAQF1AOD.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO port
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

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
        timeout = 3  ## second
        chip_select = [0]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Open AI
        err = dev.AI_open(port, timeout=timeout)
        print(f"AI_open in port {port}: {err}")
        

        ## Open AO
        err = dev.AO_open(port, timeout=timeout)
        print(f"AO_open in port {port}: {err}")

        ## Read data acquisition
        data = dev.AI_readOnDemand(port, timeout=timeout)
        print(f"AI data in port {port}: {data}")

        ## Write AO value simultaneously
        ## CH0~CH1 5V, CH2~CH3 3V, CH4~CH5 2V, CH6~CH7 0V
        err = dev.AO_writeAllChannels(port, [5,5,3,3,2,2,0,0], timeout=timeout)
        print(f"AO_writeAllChannels in port {port}: {err}")

        ## Read data acquisition
        data = dev.AI_readOnDemand(port, timeout=timeout)
        print(f"AI data in port {port}: {data}")

        ## Close AI
        err = dev.AI_close(port, timeout=timeout)
        print(f"AI_close in port {port}: {err}")

        ## Close AO
        err = dev.AO_close(port, timeout=timeout)
        print(f"AO_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()