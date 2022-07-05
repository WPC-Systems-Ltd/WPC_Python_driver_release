import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def readRSSI_loop(handle, timeout, delay): 
    t = 0
    while t < timeout:
        data = await handle.readRSSI()
        print("RSSI: " + str(data) + " dBm")
        await asyncio.sleep(delay)  ## delay(second)
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
        await readRSSI_loop(dev, 3, 0.5)
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## It will not execute because of async thread
    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__': 
    asyncio.run(main())
