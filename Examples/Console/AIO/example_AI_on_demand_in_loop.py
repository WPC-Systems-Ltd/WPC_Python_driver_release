import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, port, delay, timeout = 10):
    t = 0
    while t < timeout:
        ## data acquisition
        data =  await handle.AI_readOnDemand(port)
        print("data :" + str(data))
        await asyncio.sleep(delay)
        t += delay

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
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 1

        ## Open port 1
        status = await dev.AI_open(port)
        if status == 0: print("AI_open: OK") 
 
        ## Set AI port to 1 and start async thread
        await loop_func(dev, port, 1, 10)
    
        ## Close port 1
        status = await dev.AI_close(port) 
        if status == 0: print("AI_close: OK")
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