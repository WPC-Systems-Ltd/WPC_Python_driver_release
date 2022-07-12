import asyncio
import sys

sys.path.insert(0, 'src/')
# sys.path.insert(0, 'pywpc/')
# sys.path.insert(0, '../../../pywpc/')
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
        
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)
        print()
        print("====================")

        ## Open pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output
        ## Set pin0, pin3 and pin4 to digital high, others to digital low
        await dev.openDOInPins(0, [0,1,2,3,4], [0,3,4])

        ## Open pin4, pin5, pin6 and pin7 in port 1 with digital input 
        await dev.openDIInPins(1, [4,5,6,7])

        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 
            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 1 seconds
        await asyncio.sleep(1)  ## delay(second)

        ## Set port 0 to idle
        await dev.setPortIdle(0)
        print()
        print("====================")
                
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 
            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Close pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output 
    await dev.closeDOInPins(0, [0,1,2,3,4])

    ## Close pin4, pin5, pin6 and pin7 in port 1 with digital input
    await dev.closeDIInPins(1, [4,5,6,7])
    
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
