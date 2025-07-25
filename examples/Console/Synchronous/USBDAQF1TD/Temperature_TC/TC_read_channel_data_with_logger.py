'''
Temperature_TC - TC_read_channel_data_with_logger.py with synchronous mode.

This example demonstrates how to read thermocouple and save data into csv file from USBDAQF1TD.

First, it shows how to open thermal port and configure thermal parameters.
Second, read channel 1 thermocouple data and save them.
Last, close thermal port.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

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

    ## Create device handle
    dev = pywpc.USBDAQF1TD()

    ## Connect to device
    try:
        dev.connect("default")  ## Depend on your device
    except Exception as err:
        pywpc.printGenericError(err)
        ## Release device handle
        dev.close()
        return

    try:
        ## Parameters setting
        port = 1  ## Depend on your device
        ch = 1
        over_sampling_mode = 0  ## 0:1 sample, 1:2 samples, 2:4 sample, 3:8 samples, 4:16 samples
        thermo_type = 3  ## 0:B type, 1:E type, 2:J type, 3:K type 4:N type, 5:R type, 6:S type, 7:T type
        timeout = 3  ## [sec]

        ## Get firmware model & version
        driver_info = dev.Sys_getDriverInfo(timeout)
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Open file with WPC_test.csv
        err = dev.Logger_openFile("WPC_test.csv")

        ## Write header into CSV file
        err = dev.Logger_writeHeader(["Thermo CH1"])
        print(f"Logger_writeHeader, status: {err}")

        ## Open thermo
        err = dev.Thermal_open(port, timeout)
        print(f"Thermal_open in port {port}, status: {err}")

        ## Set thermo port and set over-sampling mode to no over-sampling in channel 1
        err = dev.Thermal_setOverSampling(port, ch, over_sampling_mode, timeout)
        print(f"Thermal_setOverSampling in channel {ch} in port {port}, status: {err}")

        ## Set thermo port and set K type in channel 1
        err = dev.Thermal_setType(port, ch, thermo_type, timeout)
        print(f"Thermal_setType in channel {ch} in port {port}, status: {err}")

        ## Wait for at least 500 ms after setting type or oversampling
        time.sleep(0.5)  ## delay [sec]

        ## Set thermo port and read thermo in channel 1
        data = dev.Thermal_readSensor(port, ch, timeout)
        print(f"Read sensor in channel {ch} in port {port}: {data} deg C")

        ## Write data into CSV file
        err = dev.Logger_writeValue(data)
        print(f"Logger_writeValue, status: {err}")

        ## Close thermo
        err = dev.Thermal_close(port, timeout)
        print(f"Thermal_close in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


if __name__ == '__main__':
    main()