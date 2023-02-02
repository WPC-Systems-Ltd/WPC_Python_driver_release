'''
Motion - Motion_1axis_move_with_S_curve_acceleration.py
 
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
        axis = 0 
        rel_posi_mode = 1
        stop_decel = 0 
        timeout = 3  ## second

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_true = 1
        reverse_enable_true = 1

        ## jerk and acceletation mode parameters setting
        scurve = 1
        jerk = 1 

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])
        
        ## Motion open
        err = dev.Motion_open_async(port, timeout)
        print("open_async:", err)
        
        ## Motion open configuration file
        err = dev.Motion_opencfgFile('3AxisStage_2P.ini', timeout)
        print("Motion_opencfgFile:", err)

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout)
        print("Motion_loadCfgFile:", err)

        ## Motion configure
        err = dev.Motion_cfgLimit(port, axis, forward_enable_true, reverse_enable_true, active_high, timeout)
        print("Motion_cfgLimit:", err)

        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_position = 5000, timeout=timeout)
        print("Motion_cfgAxisMove:", err)

        err = dev.Motion_cfgJerkAndAccelMode(port, axis, jerk, scurve, timeout)
        print("Motion_cfgJerkAndAccelMode:", err)
        
        err = dev.Motion_rstEncoderPosi(port, axis, timeout)
        print("Motion_rstEncoderPosi:", err)
        
        err = dev.Motion_enableServoOn(port, axis, int(True), timeout)
        print("Motion_enableServoOn:", err)

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout)
        print("Motion_startSingleAxisMove:", err)

        move_status = 0; 
        while move_status == 0:
            move_status = dev.Motion_getMoveStatus(port, axis, timeout)
            print("Motion_getMoveStatus:", move_status) 

        ## Motion stop         
        err = dev.Motion_stop(port, axis, stop_decel, timeout)
        print("Motion_stop:", err)

        err = dev.Motion_enableServoOn(port, axis, int(False), timeout)
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