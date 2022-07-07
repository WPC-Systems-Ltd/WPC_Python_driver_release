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
    dev = pywpc.WifiDAQ()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err) 
    
    ## Perform data acquisition
    try:  
        await dev.setAIMode(1) ## Set acquisition mode to N-samples mode (1)
        await dev.setAISamplingRate(1000) ## Set sampling rate to 1k (Hz)
        await dev.setAINumSamples(50) ## Set # of samples to 50 (pts)
        await dev.startAI() ## Start acquisition
        await asyncio.sleep(1) ## Wait amount of time (sec)
        data = await dev.readAIStreaming(50) ## Get 50 points 
        print("Get data points: " + str(len(data))) ## Read acquisition data 50 points 
        print("Get data: " + str(data))
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
