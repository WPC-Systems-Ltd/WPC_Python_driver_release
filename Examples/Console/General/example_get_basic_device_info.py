from lib2to3.pgen2 import driver
import sys
import asyncio
import os
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc


async def main():  

    print("Start example code...")
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create handle
    dev = pywpc.WifiDAQ()

    ## Connect
    try:
        dev.connect("192.168.5.79") ## Put web device's IP here
    except Exception as err:
        pywpc.printGenericError(err)

    ## Execute
    try:
        ## Get firmware model & version
        driver_info = await dev.getDriverInfo()
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
 
        ## Get serial number & RTC Time
        print(f'Serial number = ' + await dev.getSerialNumber())
        print(f'RTC data time = ' + await dev.getRTCDateTime())

        ## Get IP, submask, & MAC
        ip_addr, submask = await dev.getIPAddrAndSubmask()
        print(f'IP = ' + ip_addr)
        print(f'Submask = '+ submask)
        print(f'MAC = ' + await dev.getMACAddr())
    except Exception as err:
        pywpc.printGenericError(err)

    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
