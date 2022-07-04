import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc

async def loop_onDemand(handle, delay = 1):
    while True:
        data =  await handle.readAIOnDemand()
        print("data :" + str(data))
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

    try: 
        await loop_onDemand(dev, 1)
    except Exception as err:
        pywpc.printGenericError(err)
 
    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
