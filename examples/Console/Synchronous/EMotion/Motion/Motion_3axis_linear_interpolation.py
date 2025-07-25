'''
Motion - Motion_3axis_linear_interpolation.py with synchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        stop_decel = 0
        timeout = 3  ## [sec]

        ## Linear interpolation parameters
        axis1 = 0
        dest_posi1 = 2000
        axis2 = 1
        dest_posi2 = 2000
        axis3 = 2
        dest_posi3 = 2000

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

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
        err = dev.Motion_cfg3AxisLinearInterpo(port, axis1, dest_posi1, axis2, dest_posi2, axis3, dest_posi3, speed=2000, accel=100000, decel=100000, timeout=timeout)
        print(f"Motion_cfg3AxisLinearInterpo in port {port}, status: {err}")

        ## Motion start
        err = dev.Motion_startLinearInterpo(port, timeout)
        print(f"Motion_startLinearInterpo in port {port}, status: {err}")

        move_status = 0
        while move_status == 0:
            axis1_move_status = dev.Motion_getMoveStatus(port, axis1, timeout)
            axis2_move_status = dev.Motion_getMoveStatus(port, axis2, timeout)
            axis3_move_status = dev.Motion_getMoveStatus(port, axis3, timeout)
            move_status = axis1_move_status & axis2_move_status & axis3_move_status
            if move_status == 0:
                print("Moving......")
            else:
                print("Move completed")

        ## Motion stop
        for i in [axis1, axis2, axis3]:
            err = dev.Motion_stop(port, i, stop_decel, timeout)
            print(f"Motion_stop axis{i}, status: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()