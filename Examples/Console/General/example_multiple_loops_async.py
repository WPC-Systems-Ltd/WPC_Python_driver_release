import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def readRSSI_loop(handle, delay):
    while True:
        data = await handle.readRSSI()
        print("RSSI: " + str(data) + " dBm")
        await asyncio.sleep(delay)  ## delay(second)

async def readBattery_loop(handle, delay):
    while True:
        data = await handle.readBattery()
        print("Battery: "+ str(data) + " mV")
        await asyncio.sleep(delay)  ## delay(second)

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

    ## Perform two async thread to get data
    try:
        await asyncio.gather(readRSSI_loop(dev, delay = 1), readBattery_loop(dev, delay = 2)) ## delay (second)
    except Exception as err:
        pywpc.printGenericError(err)

    ## This part never execute because the async thread.
   
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__': 
    asyncio.run(main())
