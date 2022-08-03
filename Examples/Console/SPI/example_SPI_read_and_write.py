import asyncio
import sys
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
        dev.connect("21JA1239")
    except Exception as err:
        pywpc.printGenericError(err)
        
    try: 
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
            
        '''
        Take MAX31856 for example
        '''
        
        ## Parameters setting
        datasize = 0  ## Mode: 0 = 8-bit data, 1 = 16-bit data.
        first_bit = 0 ## Mode: 0 = MSB first, 1 = LSB first.
        prescaler = 32
        cpol = 0      ## 0 or 1
        cpha = 1      ## 0 or 1 
        SPI_port = 1
        DO_port = 2 
        DO_index = [0] ## CS pin

        ## Open pin0 in port 2 with digital output
        status = await dev.DO_openPins(DO_port, DO_index) 
        if status == 0: print("DO_openPins: OK")
 
        ## Set pin0 to high
        status = await dev.DO_writeValuePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writeValuePins: OK")

        ## Open SPI port1
        status = await dev.SPI_open(SPI_port)
        if status == 0: print("SPI_open: OK")
        
        ## Set SPI port to 1 and set datasize to 8-bit data
        status = await dev.SPI_setDataSize(SPI_port, datasize)
        if status == 0: print("SPI_setDataSize: OK")
        
        ## Set SPI port to 1 and set first_bit to MSB first
        status = await dev.SPI_setFirstBit(SPI_port, first_bit)
        if status == 0: print("SPI_setFirstBit: OK")
        
        ## Set SPI port to 1 and set prescaler to 32
        status = await dev.SPI_setPrescaler(SPI_port, prescaler)
        if status == 0: print("SPI_setPrescaler: OK")
       
        ## Set SPI port to 1 and set CPOL to 0
        status = await dev.SPI_setCPOL(SPI_port, cpol)
        if status == 0: print("SPI_setCPOL: OK")
        
        ## Set SPI port to 1 and set CPHA to 1
        status = await dev.SPI_setCPHA(SPI_port, cpha)
        if status == 0: print("SPI_setCPHA: OK")

        '''
        Read default value from address 0x00 for 1 byte (address) + 16 bytes (data)
        '''
        
        ## Set pin0 to low
        status = await dev.DO_writeValuePins(DO_port, DO_index, [0]) 
        if status == 0: print("DO_writeValuePins: OK")
 
        data = await dev.SPI_readAndWrite(SPI_port, [0x00]*17)
        print("data :", data)
        data = ['{:02x}'.format(value) for value in data]
        print("data :", data)

        ## Set pin0 to high
        status = await dev.DO_writeValuePins(DO_port, DO_index, [1])
        if status == 0: print("DO_writeValuePins: OK")
        
        ## Close pin0 in port 2 with digital output
        status = await dev.DO_closePins(DO_port, DO_index) 
        if status == 0: print("DO_closePins: OK")
        
        ## Close SPI port1
        status = await dev.SPI_close(SPI_port)
        if status == 0: print("SPI_close: OK")
        
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
