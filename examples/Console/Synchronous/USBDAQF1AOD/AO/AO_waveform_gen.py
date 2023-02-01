'''
AO - AO_waveform_gen.py
 
This example demonstrates how to use AO waveform generation in specific channels from USBDAQF1AOD.

First, it shows how to open AO in port.
Second, set AO streaming parameters
Last, close AO in port.
This example demonstrates how to write AO in all channels from USBDAQF1AOD.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
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
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
        mode = 2
        sampling_rate = 1000
        form_mode = 2 
        amplitude = 1
        offset = 0.5
        period_0 = 0.2
        period_1 = 0.1

        ## Open AO
        err = dev.AO_open(port)
        print("AO_open_async:", err)
 
        ## Set AO enabled channels
        err = dev.AO_setEnableChannels(port, [0,0,0,0,0,0,1,1]) 
        print("AO_setEnableChannels:", err)

        ## Set AO form in channel 0
        err = dev.AO_setForm(port, 0, form_mode) 
        print("AO_setForm in channel 0 :", err)

        ## Set AO form in channel 1
        err = dev.AO_setForm(port, 1, form_mode) 
        print("AO_setForm in channel 1 :", err)

        ## Set Channel 0 form parameters
        err = dev.AO_setFormParam(port, 0, amplitude, offset, period_0) 
        print("AO_setFormParam in channel 0:", err)

        ## Set Channel 1 form parameters
        err = dev.AO_setFormParam(port, 1, amplitude, offset, period_1) 
        print("AO_setFormParam in channel 1:", err)
         
        ## Set AO port and generation mode
        err = dev.AO_setMode(port, mode)
        print("AO_setMode:", err)

        ## Set AO port and sampling rate to 1k (Hz)
        err = dev.AO_setSamplingRate(port, sampling_rate)
        print("AO_setSamplingRate:", err)
                        
        ## Open AO streaming
        err = dev.AO_openStreaming(port)
        print("AO_openStreaming:", err)

        ## Start AO streaming
        err = dev.AO_startStreaming(port)
        print("AO_startStreaming:", err)

        ## Wait for 5 seconds
        time.sleep(5) 

        ## Close AO streaming
        err = dev.AO_closeStreaming(port)
        print("AO_closeStreaming:", err)
  
        ## Close AO
        err = dev.AO_close(port)
        print("AO_close:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return
if __name__ == '__main__':
    main()