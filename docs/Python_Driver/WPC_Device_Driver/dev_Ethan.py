import sys
import asyncio
sys.path.insert(0, 'src/')
# sys.path.append('build/')
# sys.path.append('pywpc/')
import pywpc

async def main():
    
    print("Start example code...")
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create handle
    dev = pywpc.EthanD()

    ## Connect
    try:
        dev.connect("192.168.1.110") ## Put web device's IP here
    except Exception as err:
        pywpc.printGenericError(err)

    ## Execute
    try: 
        ## Get firmware model & version
        driver_info = await dev.sys_getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        print(f'Serial number = ' + await dev.sys_getSerialNumber())

        network_info = await dev.sys_getIPAddrAndSubmask() 
        print(f'IP = ' + network_info[0])
        print(f'Submask = ' + network_info[1])
        print(f'MAC = ' + await dev.sys_getMACAddr())
    except Exception as err:
        pywpc.printGenericError(err) 

    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
