'''
Drone - Drone_simple_x_move.py with synchronous mode.

- Ensure the drones center of gravity is properly balanced.
- Verify that all mounted payloads are securely fastened.
- Confirm that all screws on the drone are tightened.
- Check that the drone battery is fully charged** (approximately 12.5V).
- Make sure the USB drive has sufficient storage** to record the flight data.
- Insert the USB drive into the flight control computer.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc

## Python
import time


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Parameters setting
    baudrate = 921600
    timeout = 3
    x_move = 0.3  ## [m]
    velocity = 1  ## [m/s]

    ## Create device handle
    dev = pywpc.Drone()

    ## Connect to device
    try:
        dev.connect("COM5", baudrate)  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Get firmware model & version
        firmware_version = dev.Drone_getFirmwareVersion(timeout)
        print(f"Firmware version: {firmware_version}")

        ## Get serial number
        serial_number = dev.Drone_getSerialNumber(timeout)
        print(f"Serial number: {serial_number}")

        ## Read task control mode
        control_mode = dev.Drone_readTaskControlMode(timeout)
        if control_mode == 0:
            print("Please switch the remote controller to mission computer mode.")
            print("Terminate example code. Goodbye!")
            return

        ## Set drone flight mode to position mode
        err = dev.Drone_setPositionMode(timeout)
        print(f"Drone_setPositionMode, status: {err}")

        ## Activate drone
        err = dev.Drone_activate(timeout)
        print(f"Drone_activate, status: {err}")

        ## Start drone take-off
        err = dev.Drone_startTakeOff(timeout)
        print(f"Drone_startTakeOff, status: {err}")

        ## Read drone take-off status
        takeoff_status = 0
        print("Taking off...")
        while takeoff_status == 0:
            takeoff_status = dev.Drone_getTakeOffStatus(timeout)
            if takeoff_status == 1:
                print("Completed the takeoff procedure")

        ## Wait
        print("Wait a while")
        time.sleep(5)  ## delay [sec]

        ## X move with vehicle frame
        err = dev.Drone_moveVehicleRelX(x_move, velocity, timeout)
        print(f"Drone_moveVehicleRelX, status: {err}")

        ## Read inposition
        inposition = 0
        while inposition == 0:
            posi_list = dev.Drone_readInposition(timeout)
            x_ready = posi_list[3]
            inposition = int(bool(x_ready))
            if inposition == 1:
                print("Reached X!")

    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Wait
        print("Wait a while")
        time.sleep(5)  ## delay [sec]

        ## Start landing
        err = dev.Drone_startLanding(timeout)
        print(f"Drone_startLanding, status: {err}")

        ## Read landing status
        landing_status = 0
        print("Landing....")
        while landing_status == 0:
            landing_status = dev.Drone_getLandingStatus(timeout)
            if landing_status == 1:
                print("Landing successful!")

        ## Disactivate drone
        err = dev.Drone_deactivate(timeout)
        print(f"Drone_deactivate, status: {err}")

        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

if __name__ == '__main__':
    main()