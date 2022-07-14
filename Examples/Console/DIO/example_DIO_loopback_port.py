import asyncio
import sys
# sys.path.insert(0, 'src/')
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
        
        port_DO = 0
        port_DI = 1 
        ## Open all pins in port 0 with digital output 
        await dev.DO_openPort(port_DO)

        ## Set pin0, pin1 and pin2 to high, others to low
        await dev.DO_writeValuePort(port_DO, [0,0,0,0,0,1,1,1])
       
        ## Open all pins in port 1 with digital input
        await dev.DI_openPort(port_DI)
 
        ## Read all pins state in port 1
        state_list = await dev.DI_readPort(port_DI)
        print(state_list)

        ## Wait for 3 seconds
        await asyncio.sleep(3)
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Close all pins in port 0 with digital output
    await dev.DO_closePort(port_DO)

    ## Close all pins in port 1 with digital input
    await dev.DI_closePort(port_DI)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
