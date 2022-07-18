import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, port, delay = 1):
    while True:
        ## data acquisition
        data =  await handle.AI_readOnDemand(port)
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
  
    try: 
        ## Set AI port to 1 and start async thread
        await loop_func(dev, 1, 1)
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
