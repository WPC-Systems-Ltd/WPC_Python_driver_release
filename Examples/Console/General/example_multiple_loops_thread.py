import threading
import asyncio
import sys
sys.path.insert(0, 'pywpc/')
import pywpc 
import time

async def getRSSI(handle, delay):
    data = await handle.readRSSI()
    print("RSSI: " + str(data) + " dBm")
    await asyncio.sleep(delay)  # delay(second)

async def getBattery(handle, delay):
    data = await handle.readBattery()
    print("Battery: "+ str(data) + " mV")
    await asyncio.sleep(delay)  # delay(second)

def Battery_thread(handle):
    while True: 
        asyncio.run(getBattery(handle, 0.5))
        time.sleep(1) 

def RSSI_thread(handle):
    while True: 
        asyncio.run(getRSSI(handle, 0.5))
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

        _threadBattery = threading.Thread(target = Battery_thread, args=[dev])
        _threadBattery.start()
    except Exception as err:
        pywpc.printGenericError(err) 

    ## This part will execute immediately because the sync thread is running in parallel.
    # dev.disconnect()
    # dev.close()
    # print("End example code...")

    return

if __name__ == '__main__': 
    asyncio.run(main())
