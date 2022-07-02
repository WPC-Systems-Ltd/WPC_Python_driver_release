 
import threading
import asyncio
import sys
sys.path.insert(0, 'pywpc/')
import pywpc 
import time

async def getRSSI(handle):
    data = await handle.readRSSI()
    print("RSSI: " + str(data) + " dBm")
    await asyncio.sleep(1)  ## delay(second)

def RSSI_thread(handle):
    while True:
        asyncio.run(getRSSI(handle))
        time.sleep(1)

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
        _threadRSSI = threading.Thread(target = RSSI_thread, args=[dev])
        _threadRSSI.start()
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## This part will execute immediately because the sync thread is running in parallel.
    # dev.disconnect()
    # dev.close()
    # print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
