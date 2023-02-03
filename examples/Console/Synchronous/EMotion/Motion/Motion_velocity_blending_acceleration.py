'''
Motion - Motion_velocity_blending_acceleration.py with synchronous mode.
 
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
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print("Motion_open:", err)

        ## Motion configure
        err = dev.Motion_cfgAxis(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print("Motion_cfgAxis:", err)

        err = dev.Motion_cfgAxisMove(port, axis, velocity_mode, velocity = 3000, timeout=timeout)
        print("Motion_cfgAxisMove:", err)

        err = dev.Motion_enableServoOn(port, axis, int(True), timeout)
        print("Motion_enableServoOn:", err)

        err = dev.Motion_cfgLimit(port, axis, forward_enable_true, reverse_enable_true, active_high, timeout)
        print("Motion_cfgLimit:", err)

        err = dev.Motion_cfgEncoder(port, axis, active_low, timeout)
        print("Motion_cfgEncoder:", err)

        err = dev.Motion_rstEncoderPosi(port, axis, timeout)
        print("Motion_rstEncoderPosi:", err)

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout)
        print("Motion_startSingleAxisMove:", err)
        
        time.sleep(5) 
 
        ## Motion override velocity
        new_velo = -3000
        new_accel = 100
        new_decel = 100
        err = dev.Motion_overrideAxisVelocity(port, axis, new_velo, timeout)
        print("Motion_overrideAxisVelocity:", err)

        ## Motion override acceleration
        err = dev.Motion_overrideAxisAccel(port, axis, new_accel, new_decel, timeout)
        print("Motion_overrideAxisAccel:", err)
        
        time.sleep(5) 

        new_velo = 6000
        new_accel = 100000
        new_decel = 100000
        ## Motion override velocity
        err = dev.Motion_overrideAxisVelocity(port, axis, new_velo, timeout)
        print("Motion_overrideAxisVelocity:", err)

        ## Motion override acceleration
        err = dev.Motion_overrideAxisAccel(port, axis, new_accel, new_decel, timeout)
        print("Motion_overrideAxisAccel:", err)

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