import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, num_of_samples = 600, delay = 0.05):
    while True:
        ## data acquisition
        data = await handle.AI_readStreaming(num_of_samples, delay) # Get 600 points at a time 
        print("data :" + str(data))
        await asyncio.sleep(delay)

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create device handle
    dev = pywpc.WifiDAQE3A()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err) 
    
    ## Perform data acquisition
    try:
        await dev.AI_setMode(2) ## Set acquisition mode to continuous mode (2)
        await dev.AI_setSamplingRate(1000) ## Set sampling rate to 1k (Hz)
        await asyncio.sleep(1) ## Wait amount of time (sec)
        await dev.AI_start() ## Start acquisition
        await loop_func(dev, 600, 0.05) ## Start async thread
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
