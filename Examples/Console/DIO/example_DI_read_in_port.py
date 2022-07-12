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

        ## Open all pins in port 0 with digital output 
        ## Set pin1 to digital high
        await dev.openDOInPort(0, [1])

        ## Open all pins in port 1 with digital input
        await dev.openDIInPort(1)
 
        ## Read all pins state in port 1
        state_list = await dev.readDIInPort(1)
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3)
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Close all pins in port 0 with digital output
    await dev.closeDOInPort(0)

    ## Close all pins in port 1 with digital input
    await dev.closeDIInPort(1)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
