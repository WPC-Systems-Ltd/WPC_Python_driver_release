'''
Motion - Motion_2axis_circular_interpolation.py
 
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

async def main():
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
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])
        
        ## Motion open
        err = dev.Motion_open(port, timeout)
        print("open:", err)
        
        ## Motion open configuration file
        err = dev.Motion_opencfgFile('3AxisStage_2P.ini', timeout)
        print("Motion_opencfgFile:", err)

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout)
        print("Motion_loadCfgFile:", err)
        
        ## Motion configure
        err = dev.Motion_cfgCircularInterpo(port, x_axis, y_axis, center_point_x, center_point_y, finish_point_x, finish_point_y, circular_dir_cw, speed = 1000, timeout=timeout)
        print("Motion_cfgCircularInterpo:", err) 

        err = dev.Motion_startCircularInterpo(port, timeout)
        print("Motion_startCircularInterpo:", err)

        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_position = 5000, timeout=timeout)
        print("Motion_cfgAxisMove:", err)

        err = dev.Motion_cfgJerkAndAccelMode(port, axis, jerk, scurve, timeout)
        print("Motion_cfgJerkAndAccelMode:", err)
        
        err = dev.Motion_rstEncoderPosi(port, axis, timeout)
        print("Motion_rstEncoderPosi:", err)

        for i in range(4):
            err = dev.Motion_enableServoOn(port, i, int(True), timeout)
            print("Motion_enableServoOn:", err)
            
        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout)
        print("Motion_startSingleAxisMove:", err)

        move_status = 0; 
        while move_status == 0:
            x_axis_move_status = dev.Motion_getMoveStatus(port, x_axis, timeout)
            y_axis_move_status = dev.Motion_getMoveStatus(port, y_axis, timeout)
            move_status = x_axis_move_status & y_axis_move_status;  
            if move_status == 0: 
                print("Moving......") 
            else:
                print("Move completed") 

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout)
        print("Motion_stop:", err)

        for i in range(4):
            err = dev.Motion_enableServoOn(port, i, int(False), timeout)
            print("Motion_enableServoOn:", err)
            
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