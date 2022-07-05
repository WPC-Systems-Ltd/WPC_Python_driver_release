import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def get_status(handle, delay):
    while True:
        data1 = await handle.readRSSI()
        data2 = await handle.readBattery()
        data3 = await handle.readThermo()

        print("RSSI: " + str(data1) + " dBm")
        print("Battery: "+ str(data2) + " mV")
        print("Thermo: "+ str(data3) + " °C") 
        await asyncio.sleep(delay)  ## delay(second)

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
        await get_status(dev, 1) 
    except Exception as err:
        pywpc.printGenericError(err)

    dev.disconnect()
    dev.close()
    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())
