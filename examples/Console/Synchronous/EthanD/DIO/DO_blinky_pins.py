'''
DIO - DO_blinky_pins.py with synchronous mode.

This example illustrates the process of writing a high or low signal to a DO pin from EthanD.

To begin with, it demonstrates the steps required to open the DO pin.
Next, in each loop, a different voltage output is applied, resulting in a blinking effect.
Lastly, it concludes by closing the DO pin.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EthanD()

    ## Connect to device
    try:
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        pinindex = [1, 3, 5, 7]
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Open pins with digital output
        err = dev.DO_openPins(port, pinindex, timeout)
        print(f"DO_openPins in port {port}: {err}")

        ## Toggle digital state for 10 times. Each times delay for 0.5 second
        for i in range(10):
            state = dev.DO_togglePins(port, pinindex, timeout)
            print(state)

            ## Wait for 0.5 second to see led status
            time.sleep(0.5) ## delay [s]

        ## Close pins with digital output
        err = dev.DO_closePins(port, pinindex, timeout)
        print(f"DO_closePins in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()