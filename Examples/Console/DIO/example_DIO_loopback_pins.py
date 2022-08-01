import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to network device
    try:
        dev.connect('21JA1044')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port = 0
        
        ## Open pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output
        await dev.DO_openPins(port, [0,1,2,3,4]) 

        ## Set pin0, pin1 to high, others to low.
        await dev.DO_writeValuePins(port, [0,1,2,3,4], [1,0,0,0,0]) 
        
        ## Open pin5, pin6 and pin7 in port 0 with digital output
        await dev.DI_openPins(port, [5,6,7])

        ## Read pin5, pin6 and pin7 state in port 0
        state_list = await dev.DI_readPins(port, [7,5,6])
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3) ## delay(second)

    except Exception as err:
        pywpc.printGenericError(err)

    ## Close pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output 
    await dev.DO_closePins(port, [0,1,2,3,4])

    ## Close pin5, pin6 and pin7 in port 0 with digital input
    await dev.DI_closePins(port, [5,6,7])
 
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())
