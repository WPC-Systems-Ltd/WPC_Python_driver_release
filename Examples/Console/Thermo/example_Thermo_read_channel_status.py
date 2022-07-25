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
      
        ## Open thermo
        await dev.Thermal_open()

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Get status in channel 0 
        status = await dev.Thermal_getStatus(0)
        if status == 0: print("Thermal_getStatus in chaannel 0: OK")

        ## Sleep
        await asyncio.sleep(0.1) ## delay(second)

        ## Get status in channel 1
        status = await dev.Thermal_getStatus(1)
        if status == 0: print("Thermal_getStatus in chaannel 1: OK")

    except Exception as err:
        pywpc.printGenericError(err)

    ## Close thermo
    await dev.Thermal_close()
    
    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    
    print("End example code...")
    return
if __name__ == '__main__':
    asyncio.run(main())
