import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

    ## Connect to network device
    try:
        dev.connect('21JA1239')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
      
        port = 1
        channel = 1
        ## Open thermo port
        await dev.Thermal_open(port)

        ## Set K type in channel 1 
        await dev.Thermal_setType(port, channel, 3)
        await asyncio.sleep(0.5)
        
        ## Read thermo in channel 1 for 5 times
        for i in range(5):
            data = await dev.Thermal_readCouple(port, channel)
            print("Read channel 0:", data, "°C")
            await asyncio.sleep(0.5)

        print("-------")

        ## Set B type in channel 1 
        await dev.Thermal_setType(port, channel, 0)
        await asyncio.sleep(0.5)

        ## Read thermo in channel 1 for 5 times
        for i in range(5):
            data = await dev.Thermal_readCouple(port, channel)
            print("Read channel 0:", data, "°C")
            await asyncio.sleep(0.5)


    except Exception as err:
        pywpc.printGenericError(err)

    ## Close thermo port
    await dev.Thermal_close(port)
    
    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
