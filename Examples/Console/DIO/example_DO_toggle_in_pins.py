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
        driver_info = await dev.getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pin0, pin1, pin2, pin3 in slot 0 and set it to digital output.
        ## Set pin0, pin1, pin2, pin3 to digital high.
        await dev.openDOInPins(slot = 0, pin = [0,1,2,3], pin_state = [0,1,2,3])

        ## Toggle digital output for 10 times. Each times delay for 0.5 second
        ## Toggle pin0, pin1, pin2, pin3 digital high.
        for i in range(10):
            state = await dev.toggleInPins(slot = 0, pin = [0,1,2,3])
            print(f'Slot 0, digital state = {state}') 
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 3 seconds
        await asyncio.sleep(3)  ## delay(second)
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Close pin0, pin1, pin2, pin3 in slot 0 with digital output
    await dev.closeDOInPins(slot = 0, pin = [0,1,2,3])
    
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
