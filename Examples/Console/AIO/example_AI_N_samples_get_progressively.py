import sys 
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, port = 1, timeout = 1, num_of_samples = 600, delay = 0.005):
    t = 0
    while t < timeout:
        ## data acquisition
        data = await handle.AI_readStreaming(port, num_of_samples, delay)
        if data is not None:
            print(data)
            print("Get data points: " + str(len(data)))
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

    ## Perform data acquisition
    try:
        ## Set AI port to 1 and acquisition mode to N-samples mode (1)
        await dev.AI_setMode(1, 1)

        ## Set AI port to 1 and set sampling rate to 5k (Hz)
        await dev.AI_setSamplingRate(1, 5000) 

        ## Set AI port to 1  and # of samples to 3000 (pts)
        await dev.AI_setNumSamples(1, 3000) 

        ##  Set AI port to 1 and start acquisition
        await dev.AI_start(1)

        ## Start async thread
        await loop_func(dev, 1, 1, 600, 0.005)
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
