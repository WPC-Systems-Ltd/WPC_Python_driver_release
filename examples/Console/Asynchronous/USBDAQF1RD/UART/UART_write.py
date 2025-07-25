'''
UART - UART_write.py with asynchronous mode.

This example demonstrates how to write data to another device with UART interface from USBDAQF1RD.

First, it shows how to open UART port and configure UART parameters.
Second, write bytes to another device.
Last, close UART port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc

## Python
import asyncio
import sys
sys.path.insert(0, 'src/')


async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1RD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 2  ## Depend on your device
        baudrate = 9600
        data_bit_mode = 0  ## 0 : 8-bit data, 1 : 9-bit data.
        parity_mode = 0  ## 0 : None, 2 : Even parity, 3 : Odd parity.
        stop_bit_mode = 0  ## 0 : 1 bit, 1 : 0.5 bits, 2 : 2 bits, 3 : 1.5 bits

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open UART
        err = await dev.UART_open_async(port)
        print(f"UART_open_async in port {port}, status: {err}")

        ## Set UART port and set baudrate to 9600
        err = await dev.UART_setBaudRate_async(port, baudrate)
        print(f"UART_setBaudRate_async in port {port}, status: {err}")

        ## Set UART port and set data bit to 8-bit data
        err = await dev.UART_setDataBit_async(port, data_bit_mode)
        print(f"UART_setDataBit_async in port {port}, status: {err}")

        ## Set UART port and set parity to None
        err = await dev.UART_setParity_async(port, parity_mode)
        print(f"UART_setParity_async in port {port}, status: {err}")

        ## Set UART port and set stop bit to 1 bit
        err = await dev.UART_setNumStopBit_async(port, stop_bit_mode)
        print(f"UART_setNumStopBit_async in port {port}, status: {err}")

        ## Set UART port and and write "12345" to device in string format
        err = await dev.UART_write_async(port, "12345")
        print(f"UART_write_async in port {port}, status: {err}")

        ## Set UART port and and write "chunglee people" to device
        err = await dev.UART_write_async(port, "chunglee people")
        print(f"UART_write_async in port {port}, status: {err}")

        ## Set UART port and and write "12345" to device in list format
        err = await dev.UART_write_async(port, ["1", "2", "3", "4", "5"])
        print(f"UART_write_async in port {port}, status: {err}")

        ## Close UART
        err = await dev.UART_close_async(port)
        print(f"UART_close_async in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
