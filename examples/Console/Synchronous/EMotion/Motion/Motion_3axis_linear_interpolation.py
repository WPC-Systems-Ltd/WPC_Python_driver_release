'''
Motion - Motion_3axis_linear_interpolation.py
 
For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
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
        dev.connect("192.168.1.110")
    except Exception as err:
        pywpc.printGenericError(err)

    try:
        ## Parameters setting
        port = 0
        stop_decel = 0
        timeout = 3  ## second

        ## Linear interpolation parameters
        axis1 = 0
        dest_posi1 = 2000
        axis2 = 1
        dest_posi2 = 2000 
        axis3 = 2
        dest_posi3 = 2000 
 
        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print("Motion_open:", err)

        ## Motion open configuration file
        err = dev.Motion_opencfgFile('3AxisStage_2P.ini', timeout)
        print("Motion_opencfgFile:", err)

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout)
        print("Motion_loadCfgFile:", err)

        ## Motion configure
        err = dev.Motion_cfg3AxisLinearInterpo(port, axis1, dest_posi1, axis2, dest_posi2, axis3, dest_posi3, speed = 2000, timeout=timeout)
        print("Motion_cfg3AxisLinearInterpo:", err)

        ## Motion start
        err = dev.Motion_startLinearInterpo(port, timeout)
        print("Motion_startLinearInterpo:", err)
  
        move_status = 0; 
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
            print(f"Motion_stop axis{i} :", err) 
            
        ## Motion close
        err = dev.Motion_close(port, timeout)
        print("Motion_close:", err) 
         
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return
if __name__ == '__main__':
    main()