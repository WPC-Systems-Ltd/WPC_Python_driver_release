import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def loop_func(handle, port = 1, num_of_samples = 600, delay = 0.05):
    while True:
        ## data acquisition
        data = await handle.AI_readStreaming(port, num_of_samples, delay) ## Get 600 points at a time 
        print("data :" + str(data))
        await asyncio.sleep(delay)

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
    mode = 2  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
    sampling_rate = 1000
    
    ## Perform data acquisition
    try:
        ## Set AI port to 1 and acquisition mode to continuous mode (2)
        await dev.AI_setMode(port, mode)

        ## Set AI port to 1 and sampling rate to 1k (Hz)
        await dev.AI_setSamplingRate(port, sampling_rate)

        ## Wait amount of time (sec)
        await asyncio.sleep(1)

        ## Set AI port to 1 and start acquisition
        await dev.AI_start(port)

        ## Start async thread
        await loop_func(dev, port, 600, 0.05)
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
