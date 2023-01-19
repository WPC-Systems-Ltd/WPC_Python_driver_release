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

import asyncio

## WPC

from wpcsys import pywpc

async def main():
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
        err = await dev.AO_open_async(port)
        print("AO_open_async:", err)
 
        ## Set AO enabled channels
        err = await dev.AO_setEnableChannels_async(port, [0,0,0,0,0,0,1,1]) 
        print("AO_setEnableChannels_async:", err)

        ## Set AO form in channel 0
        err = await dev.AO_setForm_async(port, 0, form_mode) 
        print("AO_setForm_async in channel 0 :", err)

        ## Set AO form in channel 1
        err = await dev.AO_setForm_async(port, 1, form_mode) 
        print("AO_setForm_async in channel 1 :", err)

        ## Set Channel 0 form parameters
        err = await dev.AO_setFormParam_async(port, 0, amplitude, offset, period_0) 
        print("AO_setForm_async in channel 0:", err)

        ## Set Channel 1 form parameters
        err = await dev.AO_setFormParam_async(port, 1, amplitude, offset, period_1) 
        print("AO_setForm_async in channel 1:", err)
         
        ## Set AO port and generation mode
        err = await dev.AO_setMode_async(port, mode)
        print("AO_setMode_async:", err)

        ## Set AO port and sampling rate to 1k (Hz)
        err = await dev.AO_setSamplingRate_async(port, sampling_rate)
        print("AO_setSamplingRate_async:", err)
                        
        ## Open AO streaming
        err = await dev.AO_openStreaming_async(port)
        print("AO_openStreaming_async:", err)

        ## Start AO streaming
        err = await dev.AO_startStreaming_async(port)
        print("AO_startStreaming_async:", err)

        ## Wait for 5 seconds
        await asyncio.sleep(5)  ## delay(second)

        ## Close AO streaming
        err = await dev.AO_closeStreaming_async(port)
        print("AO_closeStreaming_async:", err)
  
        ## Close AO
        err = await dev.AO_close_async(port)
        print("AO_close_async:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))
 
if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder