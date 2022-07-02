import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc

async def loop_fct(handle, delay):
    while True:
        print("data :" + str(await handle.readAIStreaming(600, delay)))
        await asyncio.sleep(delay)

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
        await dev.setAIMode(2) ## 2 is continuous mode
        await asyncio.sleep(1)
        await dev.startAI()
        await loop_fct(dev, 0.05)   ## 0.05s = 50 ms
    except Exception as err:
        pywpc.printGenericError(err) 
 
    dev.disconnect()
    dev.close()
    print("End example code...")
    
    return

if __name__ == '__main__':
    asyncio.run(main())
