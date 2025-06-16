'''
Motion - Motion_save_configuration_file.py with synchronous mode.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2022-2025 WPC Systems Ltd. All rights reserved.
'''

## WPC
from wpcsys import pywpc


def main():
    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.EMotion()

    ## Connect to device
    try:
        dev.connect("192.168.1.110")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 0  ## Depend on your device
        axis = 0
        two_pulse_mode = 1
        rel_posi_mode = 1
        timeout = 3  ## [sec]

        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Motion open
        err = dev.Motion_open(port, timeout)
        print(f"Motion_open in port {port}, status: {err}")

        ## Motion open configuration file
        err = dev.Motion_openCfgFile('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"Motion_openCfgFile, status: {err}")

        ## Motion configure
        err = dev.Motion_cfgAxis(port, axis, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low, timeout)
        print(f"Motion_cfgAxis in axis{axis}, status: {err}")

        err = dev.Motion_cfgAxisMove(port, axis, rel_posi_mode, target_posi=5000, velo=10000, accel=100000, decel=100000, timeout=timeout)
        print(f"Motion_cfgAxisMove in axis{axis}, status: {err}")

        ## Motion save configuration file
        err = dev.Motion_saveCfgFile(timeout)
        print(f"Motion_saveCfgFile, status: {err}")

        ## Motion close
        err = dev.Motion_close(port, timeout)
        print(f"Motion_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()