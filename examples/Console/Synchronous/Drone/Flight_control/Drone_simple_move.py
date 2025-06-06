'''
Flight_control - Drone_active.py with synchronous mode.



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
    flight_mode = 1
    x_move = 0.5 ## [m]
    velocity = 1 ## [m/s]

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


        ## Read drone flight mode
        drone_flight_mode = dev.Drone_readFlightMode(timeout)
        if drone_flight_mode == 0:
            print("Please turn to position mode.")

            ## Write drone flight mode to position mode
            err = dev.Drone_writeFlightMode(flight_mode, timeout)
            print(f"Drone_writeFlightMode, status: {err}")

            return
        else:
            print("It is on position mode.")

        ## Activate drone
        err = dev.Drone_activate(timeout)
        print(f"Drone_activate, status: {err}")


        ## Read drone activate status
        activate_status = dev.Drone_readActivateStatus(timeout)
        if activate_status == 0:
            print("Please activate the drone.")

            ## Activate drone
            err = dev.Drone_activate(timeout)
            print(f"Drone_activate, status: {err}")
            return
        else:
            print("Activated.")

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

        ## X move with vehicle frame
        err = dev.Drone_moveVehicleRelX(x_move, velocity, timeout)
        print(f"Drone_moveVehicleRelX, status: {err}")


        ## Read inposition
        x_inposition = 0
        while x_inposition == 0:
            x_inposition = dev.Drone_readInposition(timeout)[3]
            if x_inposition == 0:
                print(f"Waiting....")
            else:
                print(f"Done!")

        ## Start drone landing
        err = dev.Drone_startLanding(timeout)
        print(f"Drone_startLanding, status: {err}")

        ## Read landing status
        landing_status = 0
        while landing_status != 3:
            landing_status = dev.Drone_readStatus(timeout)[3]
            if landing_status != 3:
                print(f"Waiting....")
            else:
                print(f"Done!")

        ## Disactivate drone
        err = dev.Drone_disactivate(timeout)
        print(f"Drone_disactivate, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

if __name__ == '__main__':
    main()