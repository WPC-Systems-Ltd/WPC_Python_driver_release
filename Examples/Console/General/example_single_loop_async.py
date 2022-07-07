import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_fct(handle, timeout, delay): 
    t = 0
    while t < timeout: ## timeout(second)
        data = await handle.readRSSI()
        print("RSSI: " + str(data) + " dBm")
        await asyncio.sleep(delay)  ## delay(second)
        t += delay
 
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

    ## Perform async thread to query data
    try: 
        await loop_fct(dev, timeout = 3, delay = 0.5) ## timeout, delay(second)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## This part never execute because the async thread
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return


if __name__ == '__main__': 
    asyncio.run(main())
