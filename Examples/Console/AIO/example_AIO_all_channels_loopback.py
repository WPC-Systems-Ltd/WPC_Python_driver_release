import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1AOD()

    ## Connect to network device
    try:
        dev.connect("21JA1439")
    except Exception as err:
        pywpc.printGenericError(err)
        
    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0

        ## Open port 0
        status = await dev.AI_open(port)
        if status == 0: print("AI_open: OK")

        status = await dev.AO_open(port)
        if status == 0: print("AO_open: OK")

        ## Set AI port to 0 and data acquisition
        data = await dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Set AO port to 0 and write data simultaneously
        status = await dev.AO_writeAllChannels(port, [0,1,2,3,4,5,4,3])
        if status == 0: print("AO_writeAllChannels: OK")

        ## Sleep
        await asyncio.sleep(1) ## delay(second)

        ## Set AI port to 0 and data acquisition
        data = await dev.AI_readOnDemand(port)
        print("data :" + str(data))

        ## Close AI port 0
        status = await dev.AI_close(port) 
        if status == 0: print("AI_close: OK")

        ## Close AO port 0
        status = await dev.AO_close(port) 
        if status == 0: print("AO_close: OK") 
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    print("End example code...")
    return
    
if __name__ == '__main__':
    asyncio.run(main())
