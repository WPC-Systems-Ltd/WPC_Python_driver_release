import sys
import asyncio
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.Broadcaster()

    ## Connect to network device
    try:
        dev.connect()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform device information
    try:
        print(f'Broadcast -' + str(await dev.Bcst_getDeviceInfo()))
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
