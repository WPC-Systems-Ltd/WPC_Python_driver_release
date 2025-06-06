'''
Flight_control - Drone_takeoff.py with synchronous mode.



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

    ## Parameters setting
    baudrate = 921600
    timeout = 3

    ## Create device handle
    dev = pywpc.Drone()

    ## Connect to device
    try:
        dev.connect("COM42", baudrate) ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Read task control mode
        control_mode = dev.Drone_readTaskControlMode(timeout)
        if control_mode == 0:
            print("Please turn to mission computer mode.")
            return
        else:
            print("It is on mission computer mode.")

        ## Read drone take-off status
        activate_status = dev.Drone_readTakeOffStatus(timeout)
        print(f"Drone_readTakeOffStatus: {activate_status}")

        ## Start drone take-off
        err = dev.Drone_startTakeOff(timeout)
        print(f"Drone_startTakeOff, status: {err}")

        ## Read drone take-off status
        activate_status = 1
        while activate_status:
            activate_status = dev.Drone_readTakeOffStatus(timeout)
            if activate_status == 1:
                print("Running")
            else:
                print("Not in the takeoff procedure")

        ## Wait a while
        time.sleep(3) ## delay [s]

        ## Read landing status
        landing_status = 0
        while landing_status != 3:
            landing_status = dev.Drone_readStatus(timeout)[3]
            if landing_status != 3:
                print(f"Waiting....")
            else:
                print(f"Done!")

        ## Read drone take-off status
        activate_status = dev.Drone_readTakeOffStatus(timeout)
        print(f"Drone_readTakeOffStatus: {activate_status}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

if __name__ == '__main__':
    main()