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
        
        ## Open all pins in port 0 and set it to digital output
        status = await dev.DO_openPort(port)
        if status == 0: print("DO_openPins: OK")
        
        ## Set pin0, pin3 and pin4 to high, others to low
        status = await dev.DO_writePort(port, [0,0,0,1,1,0,0,1])
        if status == 0: print("DO_openPins: OK")

        ## Wait for 5 second
        await asyncio.sleep(5)  ## delay(second)

        ## Set pin7 and pin6 to high, others to low (1100 0000 in binary) (0xC0 in hex).
        status = await dev.DO_writePort(port, 0xC0)
        if status == 0: print("DO_openPins: OK")
       
        ## Wait for 5 second
        await asyncio.sleep(5)  ## delay(second)

        ## Close all pins in port 0 with digital output
        status = await dev.DO_closePort(port)
        if status == 0: print("DO_openPins: OK")
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