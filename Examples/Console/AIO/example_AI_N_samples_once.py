import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

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
    
    ## Perform data acquisition
    try:  
        ## Set AI port to 1 and acquisition mode to N-samples mode (1)
        await dev.AI_setMode(1, 1)
        
        ## Set AI port to 1 and sampling rate to 1k (Hz)
        await dev.AI_setSamplingRate(1, 1000) 
       
        ## Set AI port to 1 and # of samples to 50 (pts)
        await dev.AI_setNumSamples(1, 150)
        
        ## Set AI port to 1 and start acquisition
        await dev.AI_start(1)
        
        ## Wait amount of time (sec)
        await asyncio.sleep(1)
        
        ## Set AI port to 1 and get 50 points 
        data = await dev.AI_readStreaming(1, 50)
        
        ## Read acquisition data 50 points 
        print("Get data points: " + str(len(data))) 
        print("Get data: " + str(data))
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
