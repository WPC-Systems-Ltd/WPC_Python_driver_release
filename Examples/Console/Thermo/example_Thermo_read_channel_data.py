import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

    ## Connect to USB device
    try:
        dev.connect('21JA1239')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port    = 1
        channel = 1 
        over_sampling_mode = 0  ## 0:1 sample, 1:2 samples, 2:4 sample, 3:8 samples, 4:16 samples
        thermo_type = 3         ## 0:B type, 1:E type, 2:J type, 3:K type
                                ## 4:N type, 5:R type, 6:S type, 7:T type
        
        ## Open thermo port1
        status = await dev.Thermal_open(port)
        if status == 0: print("Thermal_open: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)
        
        ## Set thermo port to 1 and set over-sampling mode to no over-sampling in channel 1 
        status = await dev.Thermal_setOverSampling(port, channel, over_sampling_mode)
        if status == 0: print("setOverSampling: OK")   

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)
        
        ## Set thermo port to 1 and set K type in channel 1 
        status = await dev.Thermal_setType(port, channel, thermo_type)
        if status == 0: print("setType: OK")   
 
        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Set thermo port to 1 and read thermo in channel 1
        data = await dev.Thermal_readSensor(port, channel)
        print("Read channel 1 data:", data, "°C")

        ## Close thermo port1
        status = await dev.Thermal_close(port)
        if status == 0: print("Thermal_close: OK")   
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
