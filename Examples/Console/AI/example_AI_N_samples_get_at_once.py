import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():

    print("Start example code...")
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}') 

    ## Create handle
    dev = pywpc.WifiDAQ()

    ## Connect
    try:
        dev.connect("192.168.5.79") ## Put web device's IP here
    except Exception as err:
        pywpc.printGenericError(err) 

    try:  
        await dev.setAIMode(1) ## 1 is N-samples mode
        await dev.setAISamplingRate(1000) ## 1k
        await dev.setAINumSamples(50) ## 50 points
        await dev.startAI() ## Start AI Streaming
        await asyncio.sleep(1)
        data = await dev.readAIStreaming(50) ## Get 50 points 
        print("Get data points: " + str(len(data)))
        print("Get data: " + str(data))
    except Exception as err:
        pywpc.printGenericError(err) 
    
    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
