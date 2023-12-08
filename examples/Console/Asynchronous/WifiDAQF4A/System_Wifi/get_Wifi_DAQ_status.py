'''
System_Wifi - get_Wifi_DAQ_status.py with asynchronous mode.

This example demonstrates how to get basic information such as RSSI & battery & thermo & power & charge status from WifiDAQF4A.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc

async def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.WifiDAQF4A()

    ## Connect to device
    try:
        dev.connect("192.168.5.38") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Firmware model:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Get RSSI, battery and thermo
        rssi = await dev.Wifi_readRSSI_async()
        battery = await dev.Wifi_readBattery_async()
        thermo = await dev.Wifi_readThermo_async()

        ## Get power & charge status
        power_status  = await dev.Wifi_getPowerGoodStatus_async()
        charge_status = await dev.Wifi_getChargeStatus_async()

        print(f"RSSI: {rssi} dBm")
        print(f"Battery: {battery} mV")
        print(f"Thermo: {thermo} °C")
        print(f"Power status: {power_status}")
        print(f"Charge status: {charge_status}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect network device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))

if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder