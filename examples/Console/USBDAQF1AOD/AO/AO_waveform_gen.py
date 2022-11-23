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

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    print("Start example code...")

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
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0
        mode = 2
        sampling_rate = 1000
        form_mode = 2 
        amplitude = 1
        offset = 0.5
        period_1 = 0.2
        period_2 = 0.1

        ## Open AO
        status = await dev.AO_open_async(port)
        print("AO_open_async status: ", status)
 
        ## Set AO enabled channels
        status = await dev.AO_setEnableChannels_async(port, [0,0,0,0,0,0,1,1]) 
        print("AO_setEnableChannels_async status: ", status)

        ## Set AO form
        status = await dev.AO_setForm_async(port, [0,0,0,0,0,0,1,1], form_mode) 
        print("AO_setForm_async status: ", status)

        ## Set Channel 0 form parameters
        status = await dev.AO_setFormParam_async(port, 0, amplitude, offset, period_1) 
        print("AO_setForm_async in channel 0 status: ", status)

        ## Set Channel 1 form parameters
        status = await dev.AO_setFormParam_async(port, 1, amplitude, offset, period_2) 
        print("AO_setForm_async in channel 1 status: ", status)
         
        ## Set AO port and generation mode
        status = await dev.AO_setMode_async(port, mode)
        print("AO_setMode_async status: ", status)

        ## Set AO port and sampling rate to 1k (Hz)
        status = await dev.AO_setSamplingRate_async(port, sampling_rate)
        print("AO_setSamplingRate_async status: ", status)
                        
        # Open AO streaming
        status = await dev.AO_openStreaming_async(port)
        print("AO_openStreaming_async status: ", status)

        ## Start AO streaming
        status = await dev.AO_startStreaming_async(port)
        print("AO_startStreaming_async status: ", status)

        ## Sleep 1 second
        await asyncio.sleep(1) ## delay(second) 

        ## Close AO streaming
        status = await dev.AO_closeStreaming_async(port)
        print("AO_closeStreaming_async status: ", status)
  
        ## Close AO
        status = await dev.AO_close_async(port)
        print("AO_close_async status: ", status)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())