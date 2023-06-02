'''
AO - AO_waveform_gen.py with synchronous mode.

This example demonstrates the process of writing AO signal of STEM.
To begin with, it demonstrates the steps to open the AO port and configure the AO parameters.
Next, it outlines the procedure for AO streaming.
Finally, it concludes by explaining how to close the AO port.

If your product is "STEM", please invoke the function `Sys_setPortAIOMode`.

--------------------------------------------------------------------------------------
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
        mode = 2
        sampling_rate = 1000
        timeout = 3  ## second
        form_mode = 2
        amplitude = 1
        offset = 0.5
        period_0 = 0.2
        period_1 = 0.1

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
        
        ## Open AO
        err = dev.AO_open(port, timeout=timeout)
        print(f"AO_open in port {port}: {err}")

        ## Set AO enabled channels
        err = dev.AO_setEnableChannels(port, [0,1], timeout=timeout)
        print(f"AO_setEnableChannels in port {port}: {err}")

        ## Set AO form in channel 0
        err = dev.AO_setForm(port, 0, form_mode, timeout=timeout)
        print(f"AO_setForm in channel 0 in port {port}: {err}")

        ## Set AO form in channel 1
        err = dev.AO_setForm(port, 1, form_mode, timeout=timeout)
        print(f"AO_setForm in channel 1 in port {port}: {err}")

        ## Set Channel 0 form parameters
        err = dev.AO_setFormParam(port, 0, amplitude, offset, period_0, timeout=timeout)
        print(f"AO_setFormParam in channel 0 in port {port}: {err}")

        ## Set Channel 1 form parameters
        err = dev.AO_setFormParam(port, 1, amplitude, offset, period_1, timeout=timeout)
        print(f"AO_setFormParam in channel 1 in port {port}: {err}")

        ## Set AO port and generation mode
        err = dev.AO_setMode(port, mode, timeout=timeout)
        print(f"AO_setMode in port {port}: {err}")

        ## Set AO port and sampling rate to 1k (Hz)
        err = dev.AO_setSamplingRate(port, sampling_rate, timeout=timeout)
        print(f"AO_setSamplingRate in port {port}: {err}")

        ## Open AO streaming
        info = dev.AO_openStreaming(port, timeout=timeout)
        print(f"mode {info[0]}, sampling rate {info[1]}")

        ## Start AO streaming
        err = dev.AO_startStreaming(port)
        print(f"AO_startStreaming in port {port}: {err}")

        ## Wait for 5 seconds
        time.sleep(5) ## delay [s]

        ## Close AO streaming
        err = dev.AO_closeStreaming(port, timeout=timeout)
        print(f"AO_closeStreaming in port {port}: {err}")

        ## Close AO
        err = dev.AO_close(port)
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