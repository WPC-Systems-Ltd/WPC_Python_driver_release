'''
AO - AO_waveform_gen.py with asynchronous mode.

This example demonstrates how to use AO waveform generation in specific channels from EthanO.

First, it shows how to open AO in port.
Second, set AO streaming parameters
Last, close AO in port.
This example demonstrates how to write AO in all channels from EthanO.

Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python

import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanO()

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
        mode = 2
        sampling_rate = 1000
        form_mode = 2
        amplitude = 1
        offset = 0.5
        period_0 = 0.2
        period_1 = 0.1

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        

        ## Open AO
        err = await dev.AO_open_async(port)
        print(f"AO_open_async in port {port}: {err}")

        ## Set AO enabled channels
        err = await dev.AO_setEnableChannels_async(port, [0, 1])
        print(f"AO_setEnableChannels_async in port {port}: {err}")

        ## Set AO form in channel 0
        err = await dev.AO_setForm_async(port, 0, form_mode)
        print(f"AO_setForm_async in channel 0 in port {port}: {err}")

        ## Set AO form in channel 1
        err = await dev.AO_setForm_async(port, 1, form_mode)
        print(f"AO_setForm_async in channel 1 in port {port}: {err}")

        ## Set Channel 0 form parameters
        err = await dev.AO_setFormParam_async(port, 0, amplitude, offset, period_0)
        print(f"AO_setForm_async in channel 0 in port {port}: {err}")

        ## Set Channel 1 form parameters
        err = await dev.AO_setFormParam_async(port, 1, amplitude, offset, period_1)
        print(f"AO_setForm_async in channel 1 in port {port}: {err}")

        ## Set AO port and generation mode
        err = await dev.AO_setMode_async(port, mode)
        print(f"AO_setMode_async in port {port}: {err}")

        ## Set AO port and sampling rate to 1k (Hz)
        err = await dev.AO_setSamplingRate_async(port, sampling_rate)
        print(f"AO_setSamplingRate_async in port {port}: {err}")

        ## Open AO streaming
        info = await dev.AO_openStreaming_async(port)
        print(f"mode {info[0]}, sampling rate {info[1]}")

        ## Start AO streaming
        err = await dev.AO_startStreaming_async(port)
        print(f"AO_startStreaming_async in port {port}: {err}")

        ## Wait for 5 seconds
        await asyncio.sleep(5)  ## delay [s]

        ## Close AO streaming
        err = await dev.AO_closeStreaming_async(port)
        print(f"AO_closeStreaming_async in port {port}: {err}")

        ## Close AO
        err = await dev.AO_close_async(port)
        print(f"AO_close_async in port {port}: {err}")
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