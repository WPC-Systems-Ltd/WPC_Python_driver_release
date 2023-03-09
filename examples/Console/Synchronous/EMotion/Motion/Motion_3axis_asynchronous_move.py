'''
Motion - Motion_3axishronous_move.py with synchronous mode.

Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import threading
import time
import asyncio

## WPC

from wpcsys import pywpc



def Axis1_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = handle.Motion_getMoveStatus(port, axis)
        if move_status != 0:
            print(f"Move completed axis {axis}...")
            return move_status

        ## Wait for seconds
        time.sleep(delay) ## delay [s]

def Axis2_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = handle.Motion_getMoveStatus(port, axis)
        if move_status != 0:
            print(f"Move completed axis {axis}...")
            return move_status

        ## Wait for seconds
        time.sleep(delay) ## delay [s]

def Axis3_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = handle.Motion_getMoveStatus(port, axis)
        if move_status != 0:
            print(f"Move completed axis {axis}...")
            return move_status

        ## Wait for seconds
        time.sleep(delay) ## delay [s]

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
        axis1 = 0
        axis2 = 1
        axis3 = 2
        two_pulse_mode = 1
        rel_posi_mode = 1
        stop_decel = 0
        timeout = 3  ## second

        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_false = 0
        reverse_enable_false = 0

        ## Define Axis1 ~ Axis3 thread
        thread_1 = threading.Thread(target = Axis1_thread, args=[dev, port, axis1, 0.005])
        thread_2 = threading.Thread(target = Axis2_thread, args=[dev, port, axis2, 0.005])
        thread_3 = threading.Thread(target = Axis3_thread, args=[dev, port, axis3, 0.005])

        ## Thread start
        thread_1.start()
        thread_2.start()
        thread_3.start()

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port{port}: {err}")

        ## Motion configure for axis1
        err = dev.Motion_cfgAxis(port, axis1, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print(f"Motion_cfgAxis axis1 in port{port}: {err}")

        err = dev.Motion_cfgLimit(port, axis1, forward_enable_false, reverse_enable_false, active_low, timeout)
        print(f"Motion_cfgLimit axis1 in port{port}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis1, timeout)
        print(f"Motion_rstEncoderPosi axis1 in port{port}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis1, rel_posi_mode, target_position = 1000, timeout=timeout)
        print(f"Motion_cfgAxisMove axis1 in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis1, int(True), timeout)
        print(f"Motion_enableServoOn axis1 in port{port}: {err}")

        ## Motion start for axis1
        err = dev.Motion_startSingleAxisMove(port, axis1, timeout)
        print(f"Motion_startSingleAxisMove axis1 in port{port}: {err}")

        ## Motion configure for axis2
        err = dev.Motion_cfgAxis(port, axis2, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print(f"Motion_cfgAxis axis2 in port{port}: {err}")

        err = dev.Motion_cfgLimit(port, axis2, forward_enable_false, reverse_enable_false, active_low, timeout)
        print(f"Motion_cfgLimit axis2 in port{port}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis2, timeout)
        print(f"Motion_rstEncoderPosi axis2 in port{port}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis2, rel_posi_mode, target_position = 1000, timeout=timeout)
        print(f"Motion_cfgAxisMove axis2 in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis2, int(True), timeout)
        print(f"Motion_enableServoOn axis2 in port{port}: {err}")

        ## Motion start for axis2
        err = dev.Motion_startSingleAxisMove(port, axis2, timeout)
        print(f"Motion_startSingleAxisMove axis2 in port{port}: {err}")

        ## Motion configure for axis3
        err = dev.Motion_cfgAxis(port, axis3, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print(f"Motion_cfgAxis axis3 in port{port}: {err}")

        err = dev.Motion_cfgLimit(port, axis3, forward_enable_false, reverse_enable_false, active_low, timeout)
        print(f"Motion_cfgLimit axis3 in port{port}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis3, timeout)
        print(f"Motion_rstEncoderPosi axis3 in port{port}: {err}")

        err = dev.Motion_cfgAxisMove(port, axis3, rel_posi_mode, target_position = -5000, timeout=timeout)
        print(f"Motion_cfgAxisMove axis3 in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis3, int(True), timeout)
        print(f"Motion_enableServoOn axis3 in port{port}: {err}")

        ## Motion start for axis3
        err = dev.Motion_startSingleAxisMove(port, axis3, timeout)
        print(f"Motion_startSingleAxisMove axis3 in port{port}: {err}")

        ## Wait for thread completion
        thread_1.join()
        print("Axis1_Thread returned.")

        thread_2.join()
        print("Axis2_Thread returned.")

        thread_3.join()
        print("Axis3_Thread returned.")

        for i in [axis1, axis2, axis3]:
            err = dev.Motion_enableServoOn(port, i, int(False), timeout)
            print(f"Motion_enableServoOn axis{i}  in port{port}: {err}")

        ## Motion stop
        for i in [axis1, axis2, axis3]:
            err = dev.Motion_stop(port, i, stop_decel, timeout)
            print(f"Motion_stop axis{i}  in port{port}: {err}")

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