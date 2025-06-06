'''
Motion - Motion_3axis_helical_interpolation.py with synchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
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
        timeout = 3 ## second

        ## Helical parameters
        center_x = 0
        center_y = 0
        finish_x = 100
        finish_y = 100
        pitch_axis3 = 0
        pitch_axis4 = 0
        rotation_num = 0
        speed = 0
        cal_timeout = 1000
        helical_dir_cw = 0

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port {port}, status: {err}")

        ## Motion open configuration file
        err = dev.Motion_openCfgFile('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"Motion_openCfgFile, status: {err}")

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout)
        print(f"Motion_loadCfgFile, status: {err}")

        ## Motion configure
        err = dev.Motion_cfgHelicalInterpo(port, center_x, center_y, finish_x, finish_y, int(False), pitch_axis3, int(False), pitch_axis4, rotation_num,
        speed, helical_dir_cw, cal_timeout, timeout)
        print(f"Motion_cfgHelicalInterpo in axis{axis}, status: {err}")

        ## Motion start
        err = dev.Motion_startHelicalInterpo(port, timeout)
        print(f"Motion_startHelicalInterpo in axis{axis}, status: {err}")

        move_status = 0
        while move_status == 0:
            move_status = dev.Motion_getMoveStatus(port, axis, timeout)
            if move_status != 0:
                print(f"Move completed axis {axis}...")
                return move_status

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout)
        print(f"Motion_stop in axis{axis}, status: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()

    return

if __name__ == '__main__':
    main()