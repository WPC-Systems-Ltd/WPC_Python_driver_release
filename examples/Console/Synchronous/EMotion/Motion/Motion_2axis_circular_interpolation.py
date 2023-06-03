'''
Motion - Motion_2axis_circular_interpolation.py with synchronous mode.

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
        stop_decel = 0
        rel_posi_mode = 1
        timeout = 3  ## second

        ## Circular interpolation parameters
        x_axis = 0
        y_axis = 1
        center_point_x = 2000
        center_point_y = 2000
        finish_point_x = 0
        finish_point_y = 0
        circular_dir_cw = 0

        ## jerk and acceletation mode parameters setting
        scurve = 1
        jerk = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout=timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout=timeout)
        print(f"Motion_open in port {port}: {err}")

        ## Motion open configuration file
        err = dev.Motion_openCfgFile('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"Motion_openCfgFile: {err}")

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout=timeout)
        print(f"Motion_loadCfgFile: {err}")

        ## Motion configure
        err = dev.Motion_cfgCircularInterpo(port, x_axis, y_axis, center_point_x, center_point_y, finish_point_x, finish_point_y, circular_dir_cw, speed=1000, accel=100000, decel=100000, timeout=timeout)
        print(f"Motion_cfgCircularInterpo in port {port}: {err}")

        err = dev.Motion_startCircularInterpo(port, timeout=timeout)
        print(f"Motion_startCircularInterpo in axis{axis}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_posi=5000, velo=10000, accel=100000, decel=100000, timeout=timeout)
        print(f"Motion_cfgAxisMove in axis{axis}: {err}")

        err = dev.Motion_cfgJerkAndAccelMode(port, axis, jerk, scurve, timeout=timeout)
        print(f"Motion_cfgJerkAndAccelMode in axis{axis}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis, encoder_posi=0, timeout=timeout)
        print(f"Motion_rstEncoderPosi in axis{axis}: {err}")

        for i in range(4):
            err = dev.Motion_enableServoOn(port, i, timeout=timeout)
            print(f"Motion_enableServoOn in axis{i}: {err}")

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout=timeout)
        print(f"Motion_startSingleAxisMove in axis{axis}: {err}")

        move_status = 0
        while move_status == 0:
            x_axis_move_status = dev.Motion_getMoveStatus(port, x_axis, timeout=timeout)
            y_axis_move_status = dev.Motion_getMoveStatus(port, y_axis, timeout=timeout)
            move_status = x_axis_move_status & y_axis_move_status
            if move_status == 0:
                print("Moving......")
            else:
                print("Move completed")

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout=timeout)
        print(f"Motion_stop in axis{axis}: {err}")

        for i in range(4):
            err = dev.Motion_enableServoOff(port, i, timeout=timeout)
            print(f"Motion_enableServoOff in axis{i}: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout=timeout)
        print(f"Motion_close in port {port}: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()