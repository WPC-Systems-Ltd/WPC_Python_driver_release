import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1CD()

    ## Connect to USB device
    try:
        dev.connect('21JA1320')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get Firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Parameters setting
        port  = 1
        speed = 0 ## 0 = 125 KHz, 1 = 250 kHz, 2 = 500 kHz, 3 = 1 MHz

        ## Open CAN port1
        status = await dev.CAN_open(port) 
        if status == 0: print("CAN_open: OK")

        ## Set CAN port to 1 and set speed to 0  
        status = await dev.CAN_setSpeed(port, speed) 
        if status == 0: print("CAN_setSpeed: OK")

        ## Set CAN port to 1 and start CAN
        status = await dev.CAN_start(port) 
        if status == 0: print("CAN_start: OK")
 
        ## CAN_length: True: Extended, False: Standard 
        ## CAN_type:   True: Remote, False: Data

        ## ID: 10, data with 8 bytes, Standard & Data 
        status = await dev.CAN_write(port, 10, [33,22,11,88,77,55,66], CAN_length = False, CAN_type = False)
        if status == 0: print("CAN_write: OK")
        await asyncio.sleep(1)  ## delay(second)

        ## ID: 20, data with 8 bytes, Extended & Remote 
        status = await dev.CAN_write(port, 20, [5,20,12,58,88,22,99,77], CAN_length = True, CAN_type = True)
        if status == 0: print("CAN_write: OK")
        await asyncio.sleep(1)  ## delay(second)

        ## ID: 30, data less than 8 bytes, Standard & Data
        status = await dev.CAN_write(port, 30, [1,2,3], CAN_length = False, CAN_type = False)
        if status == 0: print("CAN_write: OK")
        await asyncio.sleep(1)  ## delay(second)
        
        ## ID: 40, data more than 8 bytes, Standard & Data
        status = await dev.CAN_write(port, 40, [1,2,3,4,5,6,7,8,9,10,11,12,13,15], CAN_length = False, CAN_type = False)
        if status == 0: print("CAN_write: OK")
        await asyncio.sleep(1)  ## delay(second)

        ## Set CAN port to 1 and stop CAN  
        status = await dev.CAN_stop(port) 
        if status == 0: print("CAN_stop: OK")
        
        ## Close CAN port1
        status = await dev.CAN_close(port) 
        if status == 0: print("CAN_close: OK")
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Disconnect USB device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())
