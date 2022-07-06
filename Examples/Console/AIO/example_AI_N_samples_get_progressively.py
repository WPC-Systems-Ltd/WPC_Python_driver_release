import sys 
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def getAIData(handle, timeout, delay):
    t = 0
    while t < timeout:
        data = await handle.readAIStreaming(600, delay=delay)
        if data is not None:
            print(data)
            print("Get data points: " + str(len(data)))
        t += delay

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

    ## Execute
    try: 
        await dev.setAIMode(1) ## 1 is N-samples mode 
        await dev.setAISamplingRate(5000) ## 5k
        await dev.setAINumSamples(2000)
        await dev.startAI() ## Start AI Streaming 
        await getAIData(dev, 1, 0.005)
    except Exception as err:
        pywpc.printGenericError(err) 

    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__': 
    asyncio.run(main())
