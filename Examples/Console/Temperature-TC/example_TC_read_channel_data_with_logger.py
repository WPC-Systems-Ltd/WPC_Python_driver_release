'''
Temperature-TC - example_TC_read_channel_data_with_logger.py

This example demonstrates how to read thermocouple and save data into csv file from WPC-USB-DAQ-F1-TD.

First, it shows how to open thermal port and configure thermal parameters.
Second, read channel 1 thermocouple data and save them. 
Last, close thermal port.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

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

    ## Create datalogger handle 
    dev_logger = pywpc.DataLogger()

    ## Open file with WPC_test.csv
    dev_logger.Logger_openFile("WPC_test.csv")

    ## Write header into CSV file
    dev_logger.Logger_writeHeader(["Thermo CH1"])

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

    ## Connect to USB device
    try:
        dev.connect('21JA1239')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 1
        channel = 1 
        over_sampling_mode = 0  ## 0:1 sample, 1:2 samples, 2:4 sample, 3:8 samples, 4:16 samples
        thermo_type = 3         ## 0:B type, 1:E type, 2:J type, 3:K type
                                ## 4:N type, 5:R type, 6:S type, 7:T type
        
        ## Open thermo port1
        status = await dev.Thermal_open_async(port)
        if status == 0: print("Thermal_open: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)
        
        ## Set thermo port to 1 and set over-sampling mode to no over-sampling in channel 1 
        status = await dev.Thermal_setOverSampling_async(port, channel, over_sampling_mode)
        if status == 0: print("setOverSampling: OK")   

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)
        
        ## Set thermo port to 1 and set K type in channel 1 
        status = await dev.Thermal_setType_async(port, channel, thermo_type)
        if status == 0: print("setType: OK")   
 
        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port to 1 and read thermo in channel 1
        data = await dev.Thermal_readSensor_async(port, channel)
        print("Read channel 1 data:", data, "°C")

        ## Write data into CSV file
        dev_logger.Logger_writeValue(data)

        ## Close thermo port1
        status = await dev.Thermal_close_async(port)
        if status == 0: print("Thermal_close: OK")

        ## Close File
        dev_logger.Logger_closeFile()  
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return
    
if __name__ == '__main__':
    asyncio.run(main())