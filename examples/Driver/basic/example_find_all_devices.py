import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc

async def main():

    print("Start example code...")
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create handle
    dev = pywpc.Broadcaster()

    ## Connect
    try:
        dev.connect()
    except Exception as err:
        pywpc.printGenericError(err)

    ## Execute
    try:
        print(f'Broadcast -' + str(await dev.getDeviceInfo()))
    except Exception as err:
        pywpc.printGenericError(err)

    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
