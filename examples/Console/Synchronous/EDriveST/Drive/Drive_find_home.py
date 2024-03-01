'''
Drive - Drive_find_home.py with synchronous mode.

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
        searching_speed = 10000
        approaching_speed = 10000
        acceleration = 10000
        search_direction = 1    ## 1: pointing to forward, -1: pointing to reverse.
        approach_direction = 1  ## 1: pointing to forward, -1: pointing to reverse.
        offset = 0
        reset_position = False
        en_forward = 0
        en_reverse = 0
        active_low = 0
        active_high = 1
        timeout = 3 ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open: {err}")

        ## Motion configure
        err = dev.Motion_cfgLimit(port, en_forward, en_reverse, active_low, timeout)
        print(f"Motion_cfgLimit: {err}")

        ## Motion reset
        err = dev.Motion_rstEncoderPosi(port, timeout)
        print(f"Motion_resetEncoderPosi: {err}")

        ## Motion Servo on
        err = dev.Motion_enableServoOn(port, timeout)
        print(f"Motion_enableServoOn: {err}")

        ## Motion find home
        err = dev.Motion_startFindHome(port, searching_speed, approaching_speed, acceleration, search_direction, approach_direction, offset, reset_position, timeout)
        print(f"Motion_startFindHome: {err}")

        status = 1
        while status != 0 :
            status = dev.Motion_getProcessState(port, timeout)

        ## Motion get limit status
        state_list = dev.Motion_getLimitStatus(port, timeout)
        print(f"Forward limit status: {state_list[0]}")
        print(f"Reverse limit status: {state_list[1]}")
        print(f"Home status: {state_list[2]}")

    except Exception as err:
        pywpc.printGenericError(err)
    except KeyboardInterrupt:
        print("Press keyboard")
    finally:
        ## Motion stop
        err = dev.Motion_stopProcess(port, timeout)
        print(f"Motion_stopProcess: {err}")

        ## Motion Servo off
        err = dev.Motion_enableServoOff(port, timeout)
        print(f"Motion_enableServoOff: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close: {err}")

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

if __name__ == '__main__':
    main()