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

    ## Connect to network device
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

        ## CAN Open
        status = await dev.CAN_open(port) 
        if status == 0: print("CAN_open: OK")

        ## Set CAN speed to 0  
        status = await dev.CAN_setSpeed(port, speed) 
        if status == 0: print("CAN_setSpeed: OK")

        ## CAN Start
        status = await dev.CAN_start(port) 
        if status == 0: print("CAN_start: OK")

        ## Read 5 frames for 1000 times
        for i in range(1000):
            data = await dev.CAN_read(port, 5)
            if data is None:
                await asyncio.sleep(0.01)
            else:
                print(data)
            
        ## CAN Stop
        status = await dev.CAN_stop(port) 
        if status == 0: print("CAN_stop: OK")
        
        ## CAN Close
        status = await dev.CAN_close(port) 
        if status == 0: print("CAN_close: OK")
    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()
    return

if __name__ == '__main__':
    asyncio.run(main())