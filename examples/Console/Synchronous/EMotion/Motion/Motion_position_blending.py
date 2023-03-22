'''
Motion - Motion_position_blending.py with synchronous mode.

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
        rel_posi_mode = 1
        stop_decel = 0
        new_position = 0
        timeout = 3  ## second

        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1
        home_enable_false = 0

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

        err = dev.Motion_cfgHome(port, axis, home_enable_false, active_low, timeout=timeout)
        print(f"Motion_cfgHome in axis{axis}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_posi=5000, timeout=timeout)
        print(f"Motion_cfgAxisMove in axis{axis}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis, timeout=timeout)
        print(f"Motion_rstEncoderPosi in axis{axis}: {err}")

        ## Servo on
        err = dev.Motion_enableServoOn(port, axis, timeout=timeout)
        print(f"Motion_enableServoOn in axis{axis}: {err}")

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout=timeout)
        print(f"Motion_startSingleAxisMove in axis{axis}: {err}")

        move_status = 0
        while move_status == 0:
            move_status = dev.Motion_getMoveStatus(port, axis, timeout=timeout)
            logical_posi = dev.Motion_getLogicalPosi(port, axis, timeout=timeout)
            encoder_posi = dev.Motion_getEncoderPosi(port, axis, timeout=timeout)
            print(f"logical_posi: {logical_posi}, encoder_posi: {encoder_posi}")

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