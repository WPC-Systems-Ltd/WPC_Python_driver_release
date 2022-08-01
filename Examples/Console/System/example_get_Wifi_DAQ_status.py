import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, delay = 1):
    while True:
        data1 = await handle.Wifi_readRSSI()
        data2 = await handle.Wifi_readBattery()
        data3 = await handle.Wifi_readThermo()

        print("RSSI: " + str(data1) + " dBm")
        print("Battery: "+ str(data2) + " mV")
        print("Thermo: "+ str(data3) + " °C") 
        await asyncio.sleep(delay) ## delay (second)

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

    ## Perform async thread to get RSSI, Battery and Thermo in once loop
    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        await loop_func(dev, 1)  ## delay (second)
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
