'''
AI - example_AI_N_samples_once.py

This example demonstrates how to get AI data in N samples mode.
Also, it gets AI data in once with 8 channels from Wifi-DAQ-E3-A.
 
First, it shows how to open AI port and configure AI parameters.
Second, read AI streaming data .
Last, close AI port.

For other examples please check:
   https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples

   See README.md file to get detailed usage of this example.

Copyright (c) 2022 WPC Systems Ltd.
All rights reserved.

'''

## Python
import asyncio
import sys
 
## WPC
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

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 1
        mode = 1  ## 0 : On demand, 1 : N-samples, 2 : Continuous.
        sampling_rate = 1000
        samples = 50    
        read_poins = 50 

        ## Open port 1
        status = await dev.AI_open(port)
        if status == 0: print("AI_open: OK")

        ## Set AI port to 1 and acquisition mode to N-samples mode (1)
        status = await dev.AI_setMode(port, mode)
        if status == 0: print("AI_setMode: OK")

        ## Set AI port to 1 and sampling rate to 1k (Hz)
        status = await dev.AI_setSamplingRate(port, sampling_rate) 
        if status == 0: print("AI_setSamplingRate: OK")
        
        ## Set AI port to 1 and # of samples to 50 (pts)
        status = await dev.AI_setNumSamples(port, samples)
        if status == 0: print("AI_setNumSamples: OK")

        ## Set AI port to 1 and start acquisition
        status = await dev.AI_start(port)
        if status == 0: print("AI_start: OK")

        ## Wait amount of time (sec)
        await asyncio.sleep(1)
        
        ## Set AI port to 1 and get 50 points 
        data = await dev.AI_readStreaming(port, read_poins)
        
        ## Read acquisition data 50 points 
        print("Get data points: " + str(len(data))) 
        print("Get data: " + str(data))

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