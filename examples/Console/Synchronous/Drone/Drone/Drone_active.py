'''
Drone - Drone_active.py with synchronous mode.

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

        ## Read drone activate status
        activate_status = dev.Drone_readActivateStatus(timeout)
        print(f"Drone_readActivateStatus: {activate_status}")

        ## Activate drone
        err = dev.Drone_activate(timeout)
        print(f"Drone_activate, status: {err}")

        ## Read drone activate status
        activate_status = dev.Drone_readActivateStatus(timeout)
        print(f"Drone_readActivateStatus: {activate_status}")

        ## Disactivate drone
        err = dev.Drone_disactivate(timeout)
        print(f"Drone_disactivate, status: {err}")

        ## Read drone activate status
        activate_status = dev.Drone_readActivateStatus(timeout)
        print(f"Drone_readActivateStatus: {activate_status}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()

if __name__ == '__main__':
    main()