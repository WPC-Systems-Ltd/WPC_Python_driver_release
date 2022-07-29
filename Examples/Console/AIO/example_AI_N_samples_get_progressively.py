import sys 
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, port, timeout, num_of_samples = 600, delay = 0.005):
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

    ## Parameters setting
    port = 1  ## Set AI port to 1 in WifiDAQE3A
    mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
    sampling_rate = 5000
    samples = 3000

    ## Perform data acquisition
    try:
        ## Set AI port to 1 and acquisition mode to N-samples mode (1)
        await dev.AI_setMode(port, mode)

        ## Set AI port to 1 and set sampling rate to 5k (Hz)
        await dev.AI_setSamplingRate(port, sampling_rate) 

        ## Set AI port to 1  and # of samples to 3000 (pts)
        await dev.AI_setNumSamples(port, samples) 

        ##  Set AI port to 1 and start acquisition
        await dev.AI_start(port)

        ## Start async thread
        await loop_func(dev, port, 1, 600, 0.005)
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
