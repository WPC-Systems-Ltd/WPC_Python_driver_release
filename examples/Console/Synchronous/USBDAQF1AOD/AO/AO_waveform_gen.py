
'''
AO - AO_waveform_gen.py with synchronous mode.

This example demonstrates the process of writing AO signal of USBDAQF1AOD.
To begin with, it demonstrates the steps to open AO and configure the AO parameters.
Next, it outlines the procedure for AO streaming.
Finally, it concludes by explaining how to close AO.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
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
        mode = 2 ## 0: on demand, 1: N-samples, 2: Continuous
        sampling_rate = 10000
        number_of_sample = 10000
        form_mode = 3 ##  0:DC voltage, 1: retangular, 2: triangular, 3: sine.
        amplitude = 1
        offset = 0.1
        freq_0 = 10
        freq_1 = 20
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open AO
        err = dev.AO_open(port, timeout)
        print(f"AO_open in port {port}: {err}")

        ## Set AO generation mode
        err = dev.AO_setMode(port, mode, timeout)
        print(f"AO_setMode in port {port}: {err}")

        ## Set AO sampling rate to 10k (Hz)
        err = dev.AO_setSamplingRate(port, sampling_rate, timeout)
        print(f"AO_setSamplingRate in port {port}: {err}")

        ## Set AO NumSamples to 10000
        err = dev.AO_setNumSamples(port, number_of_sample, timeout)
        print(f"AO_setNumSamples in port {port}: {err}")

        ## Set AO enabled channels
        err = dev.AO_setEnableChannels(port, [0, 1], timeout)
        print(f"AO_setEnableChannels in port {port}: {err}")

        ## Set AO form in channel 0
        err = dev.AO_setForm(port, 0, form_mode, timeout)
        print(f"AO_setForm in channel 0 in port {port}: {err}")

        ## Set AO form in channel 1
        err = dev.AO_setForm(port, 1, form_mode, timeout)
        print(f"AO_setForm in channel 1 in port {port}: {err}")

        ## Set Channel 0 form parameters
        err = dev.AO_setFormParam(port, 0, amplitude, offset, freq_0, timeout)
        print(f"AO_setFormParam in channel 0 in port {port}: {err}")

        ## Set Channel 1 form parameters
        err = dev.AO_setFormParam(port, 1, amplitude, offset, freq_1, timeout)
        print(f"AO_setFormParam in channel 1 in port {port}: {err}")

        ## Open AO streaming
        info = dev.AO_openStreaming(port, timeout)
        print(f"mode {info[0]}, sampling rate {info[1]}")

        ## Start AO streaming
        err = dev.AO_startStreaming(port)
        print(f"AO_startStreaming in port {port}: {err}")

        ## Wait for 10 seconds to generate form
        time.sleep(10) ## delay [s]

        ## Close AO streaming
        err = dev.AO_closeStreaming(port, timeout)
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
