'''
DIO - example_DO_blinky_pins.py

First, it shows how to open DO in pins.
Second, each loop has different voltage output so it will look like blinking. 
Last, close DO in pins.

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
    dev = pywpc.USBDAQF1D()

    ## Connect to USB device
    try:
        dev.connect('21JA1044')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Parameters setting
        port = 0
        pinindex = [0,7]
 
        ## Open pin0 and pin7 in port 0 with digital output
        status = await dev.DO_openPins(port, pinindex)
        if status == 0: print("DO_openPins: OK")

        for i in range(10):
            if i%2 == 0:
                value = [0,1]
            else:
                value = [1,0]

            await dev.DO_writePins(port, pinindex, value) 
            print(f'Port: {port}, pinindex = {pinindex}, digital state = {value}') 
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 3 seconds
        await asyncio.sleep(3)  ## delay(second)
        
        ## Close pin0 and pin7 in port 0 with digital output 
        status = await dev.DO_closePins(port, pinindex)
        if status == 0: print("DO_closePins: OK")
    except Exception as err:
        pywpc.printGenericError(err)
        
    ## Disconnect USB device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())