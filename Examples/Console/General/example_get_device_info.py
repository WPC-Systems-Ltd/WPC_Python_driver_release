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
    dev = pywpc.WifiDAQE3A()

    ## Connect to network device
    try:
        dev.connect("192.168.5.79")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Perform DAQ basic information 
    try:
        ## Get firmware model & version
        driver_info = await dev.sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
 
        ## Get serial number & RTC Time
        print(f'Serial number = ' + await dev.sys_getSerialNumber())
        print(f'RTC data time = ' + await dev.sys_getRTC())

        ## Get IP, submask, & MAC
        ip_addr, submask = await dev.sys_getIPAddrAndSubmask()
        print(f'IP = ' + ip_addr)
        print(f'Submask = '+ submask)
        print(f'MAC = ' + await dev.sys_getMACAddr())
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
