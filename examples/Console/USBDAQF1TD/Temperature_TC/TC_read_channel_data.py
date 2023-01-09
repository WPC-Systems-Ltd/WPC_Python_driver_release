'''
Temperature_TC - TC_read_channel_data.py

This example demonstrates how to read thermocouple from USBDAQF1TD.

First, it shows how to open thermal port and configure thermal parameters.
Second, read channel 1 thermocouple data.
Last, close thermal port.

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
    dev = pywpc.USBDAQF1TD()

    ## Connect to device
    try:
        dev.connect("21JA1239")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 1
        channel = 1
        over_sampling_mode = 0  ## 0:1 sample, 1:2 samples, 2:4 sample, 3:8 samples, 4:16 samples
        thermo_type = 3         ## 0:B type, 1:E type, 2:J type, 3:K type
                                ## 4:N type, 5:R type, 6:S type, 7:T type

        ## Open thermo
        err = await dev.Thermal_open_async(port)
        print("Thermal_open_async:", err)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port and set over-sampling mode to no over-sampling in channel 1
        err = await dev.Thermal_setOverSampling_async(port, channel, over_sampling_mode)
        print("Thermal_setOverSampling_async:", err)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port and set K type in channel 1
        err = await dev.Thermal_setType_async(port, channel, thermo_type)
        print("Thermal_setType_async:", err)

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port and read thermo in channel 1
        data = await dev.Thermal_readSensor_async(port, channel)
        print("Read channel 1 data:", data, "°C")

        ## Close thermo
        err = await dev.Thermal_close_async(port)
        print("Thermal_close_async:", err)
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    asyncio.run(main())