import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc

async def DI_loop(handle, slot, mask, timeout = 20 , delay = 0.5): 
    t = 0
    while t < timeout:
        state = await handle.readAndGetDI(slot, mask)
        print("state: ", state)
        await asyncio.sleep(delay)  ## delay(second)
        t += delay

async def DO_loop(handle, slot, mask, timeout = 20 , delay = 1): 
    t = 0
    while t < timeout:
        data = await handle.toggleAndWriteDO(slot, mask)
        await asyncio.sleep(delay)  ## delay(second)
        t += delay

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to network device
    try:
        dev.connect('21JA1044')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Set DIO current to slot 0 
        state = await dev.setDIOCurrent(0, 255, 255, 255, 255)
        print("state: ",state)

        await asyncio.gather(DO_loop(dev, 0, 255), DI_loop(dev, 0, 255))
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
