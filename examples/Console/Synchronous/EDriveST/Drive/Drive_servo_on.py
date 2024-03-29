'''
Drive - Drive_servo_on.py with synchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2024 WPC Systems Ltd. All rights reserved.
'''

## Python
import time

## WPC

from wpcsys import pywpc

def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EDriveST()

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
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open, status: {err}")

        ## Motion servo on
        err = dev.Motion_enableServoOn(port, timeout)
        print(f"Motion_enableServoOn, status: {err}")

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        ## Motion stop
        err = dev.Motion_stopProcess(port, timeout)
        print(f"Motion_stopProcess, status: {err}")

        ## Motion Servo off
        err = dev.Motion_enableServoOff(port, timeout)
        print(f"Motion_enableServoOff, status: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close, status: {err}")

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

if __name__ == '__main__':
    main()