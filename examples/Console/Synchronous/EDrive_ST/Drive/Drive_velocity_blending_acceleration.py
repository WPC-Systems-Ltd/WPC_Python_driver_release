'''
Drive - Drive_velocity_blending_acceleration.py with synchronous mode.

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
    dev = pywpc.EDrive_ST()

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
        forward = 0
        reverse = 1
        velocity_mode = 2

        ## Operation and stop mode
        stop_decel = 0
        timeout = 3 ## second

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        en_forward = 0
        en_reverse = 0

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## EDrive-ST open
        err = dev.Drive_open(port, timeout=timeout)
        print(f"Drive_open: {err}")

        ## EDrive-ST configure
        err = dev.Drive_cfgAxisMove(port, velocity_mode, timeout=timeout)
        print(f"Drive_cfgAxisMove: {err}")

        err = dev.Drive_cfgLimit(port, en_forward, en_reverse, active_low, timeout=timeout)
        print(f"Drive_cfgLimit: {err}")

        ## EDrive-ST reset
        err = dev.Drive_rstEncoderPosi(port, timeout=timeout)
        print(f"EDST_reset: {err}")

        ## EDrive-ST Servo on
        err = dev.Drive_enableServoOn(port, timeout=timeout)
        print(f"Drive_enableServoOn: {err}")

        ## EDrive-ST start
        err = dev.Drive_start(port)
        print(f"Drive_start: {err}")

        ## Wait for 5 seconds for moving
        time.sleep(5) ## delay [s]

        new_velo = -3000
        new_accel = 100
        new_decel = 100
        err = dev.Drive_overrideVelocity(port, new_velo, timeout=timeout)
        print(f"Drive_overrideVelocity: {err}")

        err = dev.Drive_overrideAccel(port, new_accel, new_decel, timeout=timeout)
        print(f"Drive_overrideAccel: {err}")

        ## Wait for 5 seconds for moving
        time.sleep(5) ## delay [s]

        new_velo = 6000
        new_accel = 100000
        new_decel = 100000
        err = dev.Drive_overrideVelocity(port, new_velo, timeout=timeout)
        print(f"Drive_overrideVelocity: {err}")

        err = dev.Drive_overrideAccel(port, new_accel, new_decel, timeout=timeout)
        print(f"Drive_overrideAccel: {err}")

        ## Wait for 5 seconds for moving
        time.sleep(5) ## delay [s]

        ## EDrive-ST Stop
        err = dev.Drive_stop(port, stop_decel, timeout=timeout)
        print(f"Drive_stop: {err}")

        ## EDrive-ST Servo off
        err = dev.Drive_enableServoOff(port, timeout=timeout)
        print(f"Drive_enableServoOff: {err}")

        ## EDrive-ST close
        err = dev.Drive_close(port, timeout=timeout)
        print(f"Drive_close: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()