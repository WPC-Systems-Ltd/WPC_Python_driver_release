'''
Motion - Motion_find_index.py with synchronous mode.

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

        ## Find index parameters
        dir_reverse = 1
        find_index = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout=timeout)
        print(f"Motion_open in port{port}: {err}")

        '''
        ## Motion open configuration file
        err = dev.Motion_openCfgFile('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"openCfgFile: {err}")

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile()
        print(f"loadCfgFile: {err}")
        '''

        ## Motion configure
        err = dev.Motion_cfgAxis(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout=timeout)
        print(f"Motion_cfgAxis in axis{axis}: {err}")

        err = dev.Motion_cfgLimit(port, axis, forward_enable_true, reverse_enable_true, active_low, timeout=timeout)
        print(f"Motion_cfgLimit in axis{axis}: {err}")

        err = dev.Motion_cfgFindRef(port, axis, find_index, dir_reverse, timeout=timeout)
        print(f"Motion_cfgFindRef in axis{axis}: {err}")

        err = dev.Motion_cfgEncoder(port, axis, active_low, timeout=timeout)
        print(f"Motion_cfgEncoder in axis{axis}: {err}")

        ## Servo on
        err = dev.Motion_enableServoOn(port, axis, timeout=timeout)
        print(f"Motion_enableServoOn in axis{axis}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis, timeout=timeout)
        print(f"Motion_rstEncoderPosi in axis{axis}: {err}")

        ## Motion find reference
        err = dev.Motion_findRef(port, axis, timeout=timeout)
        print(f"Motion_findRef in axis{axis}: {err}")

        finding = 1
        found = 0
        while found == 0:
            ## Read forward and reverse limit status
            hit_status = dev.Motion_getLimitStatus(port, axis, timeout=timeout)
            forward_hit = hit_status[0]
            reverse_hit = hit_status[1]
            if forward_hit == 1 : print("Forward hit")
            if reverse_hit == 1 : print("Reverse hit")

            ## Check finding and found status
            driving_status = dev.Motion_checkRef(port, axis, timeout=timeout)
            finding = driving_status[0]
            found = driving_status[1]
            if found == 1 : print("Found reference")
            # if finding == 1 : print("Finding reference")

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout=timeout)
        print(f"Motion_stop in axis{axis}: {err}")

        ## Servo off
        err = dev.Motion_enableServoOff(port, axis, timeout=timeout)
        print(f"Motion_enableServoOff in axis{axis}: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout=timeout)
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