'''
Motion - Motion_velocity_blending_acceleration.py with synchronous mode.

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
    dev = pywpc.EMotion()

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
        axis = 0
        two_pulse_mode = 1
        velocity_mode = 2
        stop_decel = 0
        timeout = 3  ## second

        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port{port}: {err}")

        ## Motion configure
        err = dev.Motion_cfgAxis(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print(f"Motion_cfgAxis in port{port}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis, velocity_mode, velocity = 3000, timeout=timeout)
        print(f"Motion_cfgAxisMove in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis, int(True), timeout)
        print(f"Motion_enableServoOn in port{port}: {err}")

        err = dev.Motion_cfgLimit(port, axis, forward_enable_true, reverse_enable_true, active_high, timeout)
        print(f"Motion_cfgLimit in port{port}: {err}")

        err = dev.Motion_cfgEncoder(port, axis, active_low, timeout)
        print(f"Motion_cfgEncoder in port{port}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis, timeout)
        print(f"Motion_rstEncoderPosi in port{port}: {err}")

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout)
        print(f"Motion_startSingleAxisMove in port{port}: {err}")

        ## Wait for 5 seconds for moving
        time.sleep(5) ## delay [s]

        ## Motion override velocity
        new_velo = -3000
        new_accel = 100
        new_decel = 100
        err = dev.Motion_overrideAxisVelocity(port, axis, new_velo, timeout)
        print(f"Motion_overrideAxisVelocity in port{port}: {err}")

        ## Motion override acceleration
        err = dev.Motion_overrideAxisAccel(port, axis, new_accel, new_decel, timeout)
        print(f"Motion_overrideAxisAccel in port{port}: {err}")

        ## Wait for 5 seconds for moving
        time.sleep(5) ## delay [s]

        new_velo = 6000
        new_accel = 100000
        new_decel = 100000
        ## Motion override velocity
        err = dev.Motion_overrideAxisVelocity(port, axis, new_velo, timeout)
        print(f"Motion_overrideAxisVelocity in port{port}: {err}")

        ## Motion override acceleration
        err = dev.Motion_overrideAxisAccel(port, axis, new_accel, new_decel, timeout)
        print(f"Motion_overrideAxisAccel in port{port}: {err}")

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout)
        print(f"Motion_stop in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis, int(False), timeout)
        print(f"Motion_enableServoOn in port{port}: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close in port{port}: {err}")

    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()