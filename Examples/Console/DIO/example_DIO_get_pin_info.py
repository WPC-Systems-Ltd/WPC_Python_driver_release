import sys
import asyncio
sys.path.insert(0, 'pywpc/')
import pywpc
import time

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

        ## Load DIO start up from bootloader
        print(f'Get Bootloader')
        print()
        for i in range (4):
            enabled, direction, state = await dev.loadDIOStartup(i)
            print(f'Slot {i}, enabled   = {enabled}')
            print(f'Slot {i}, direction = {direction}')
            print(f'Slot {i}, state     = {state}') 
            print()
            time.sleep(0.5)
        print("---------------------------")
         

        ## Get pinmode of slot
        for i in range (4):
            pins, pinmode_list = await dev.getPinModeOfSlot(i)
            print(f'Slot {i}, pins = {pins}, pinmode= {pinmode_list}')
            print()
            time.sleep(0.5)
        print("---------------------------")



        ## Set DIO Current
        for i in range (4):
            state = await dev.setDIOCurrent(i, 255, 170, 170, 255)
            print(f'Slot {i}, state   = {state}') 
            print()
            time.sleep(1)

        print("---------------------------")
    
      
        ## Get DIO Current
        print(f'Get Current')
        print()
        for i in range (4):
            enabled, direction, state = await dev.getDIOCurrent(i,255)
            print(f'Slot {i}, enabled   = {enabled}')
            print(f'Slot {i}, direction = {direction}')
            print(f'Slot {i}, state     = {state}') 
            print()
            time.sleep(0.5) 
        print("---------------------------")
      

        ## Get pinmode of slot
        for i in range (4):
            pins, pinmode_list = await dev.getPinModeOfSlot(i)
            print(f'Slot {i}, pins = {pins}, pinmode= {pinmode_list}')
            print()
            time.sleep(0.5)
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
