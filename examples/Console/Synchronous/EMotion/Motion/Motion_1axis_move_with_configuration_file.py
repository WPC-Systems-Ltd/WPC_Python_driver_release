'''
Motion - Motion_1axis_move_with_configuration_file.py with synchronous mode.

Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
        dev.connect("192.168.1.110") ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0 ## Depend on your device
        axis = 0
        rel_posi_mode = 1
        stop_decel = 0
        timeout = 3  ## second

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port{port}: {err}")

        ## Motion open configuration file
        err = dev.Motion_opencfgFile('3AxisStage_2P.ini', timeout)
        print(f"Motion_opencfgFile in port{port}: {err}")

        ## Motion load configuration file
        err = dev.Motion_loadCfgFile(timeout)
        print(f"Motion_loadCfgFile in port{port}: {err}")

        ## Motion configure
        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_position = 5000, timeout=timeout)
        print(f"Motion_cfgAxisMove in port{port}: {err}")

        err = dev.Motion_rstEncoderPosi(port, axis, timeout)
        print(f"Motion_rstEncoderPosi in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis, int(True), timeout)
        print(f"Motion_enableServoOn in port{port}: {err}")

        ## Motion start
        err = dev.Motion_startSingleAxisMove(port, axis, timeout)
        print(f"Motion_startSingleAxisMove in port{port}: {err}")

        move_status = 0;
        while move_status == 0:
            move_status = dev.Motion_getMoveStatus(port, axis, timeout)
            print("Motion_getMoveStatus:", move_status)

        ## Motion stop
        err = dev.Motion_stop(port, axis, stop_decel, timeout)
        print(f"Motion_stop in port{port}: {err}")

        err = dev.Motion_enableServoOn(port, axis, int(False), timeout)
        print(f"Motion_enableServoOn in port{port}: {err}")

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