'''
AIO - AIO_one_channel_loopback.py with synchronous mode.

This example demonstrates the process of AIO loopback with specific channels of STEM.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.

Initially, the example demonstrates the steps required to open the AI and AO port
Next, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on-demand data once again.
Lastly, it closes the AO and AI ports.

If your product is "STEM", please invoke the function `Sys_setPortAIOMode` and `AI_enableCS`.
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
        chip_select = [0]
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
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
        
        ## Open AO
        err = dev.AO_open(port, timeout=timeout)
        print(f"AO_open in port {port}: {err}")

        ## Read data acquisition
        data = dev.AI_readOnDemand(port, timeout=timeout)
        print(f"AI data in port {port}: {data}")

        ## Write AO vaule 1.5(V) in channel 0
        err = dev.AO_writeOneChannel(port, 0, 1.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch0 in port {port}: {err}")

        ## Write AO vaule 2.5(V) in channel 1
        err = dev.AO_writeOneChannel(port, 1, 2.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch1 in port {port}: {err}")

        ## Write AO vaule 3.5(V) in channel 2
        err = dev.AO_writeOneChannel(port, 2, 3.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch2 in port {port}: {err}")

        ## Write AO vaule 4.5(V) in channel 3
        err = dev.AO_writeOneChannel(port, 3, 4.5, timeout=timeout)
        print(f"AO_writeOneChannel in ch3 in port {port}: {err}")

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