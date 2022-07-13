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
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open all pins in port 0 and set it to digital output
        ## Set pin0, pin3 and pin4 to high, others to low
        await dev.DO_openPort(0, [0,3,4])
      
        ## Wait for 1 second
        await asyncio.sleep(1)  ## delay(second)

        ## Open all pins in port 1 and set it to digital output
        ## Set pin0, pin2, pin4 and pin6 to high, others to low (0101 0101 in binary)
        await dev.DO_openPort(1, 0x55)
 
        ## Wait for 1 second
        await asyncio.sleep(1)  ## delay(second)
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Close all pins in port 0 and port 1 with digital output
    await dev.DO_closePort(0) 
    await dev.DO_closePort(1)
    
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
