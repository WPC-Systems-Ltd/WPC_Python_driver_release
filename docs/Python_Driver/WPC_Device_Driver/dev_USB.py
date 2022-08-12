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
    dev = pywpc.USBDAQF1CD()

 
    ## Connect to USB device
    try:
        dev.connect('21JA1318')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1]) 

    except Exception as err:
        pywpc.printGenericError(err)
        
    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()

    # print("End example code...")
    # return

if __name__ == '__main__':
    asyncio.run(main())