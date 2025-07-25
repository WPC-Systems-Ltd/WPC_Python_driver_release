'''
Motion - Motion_3axis_synchronous_move.py with asynchronous mode.

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
import threading
import time
import asyncio


async def getAxisStatus(handle, port, axis, delay=0.005):
    move_status = await handle.Motion_getMoveStatus_async(port, axis)
    if move_status != 0:
        print(f"Move completed axis {axis}...")

    ## Wait for seconds
    await asyncio.sleep(delay)   ## delay [sec]
    return move_status


def Axis1_thread(handle, port, axis, delay=0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))

        ## Wait for seconds
        time.sleep(delay)  ## delay [sec]


def Axis2_thread(handle, port, axis, delay=0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))

        ## Wait for seconds
        time.sleep(delay)  ## delay [sec]


def Axis3_thread(handle, port, axis, delay=0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))

        ## Wait for seconds
        time.sleep(delay)  ## delay [sec]


async def main():
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
        axis1 = 0
        axis2 = 1
        axis3 = 2
        two_pulse_mode = 1
        rel_posi_mode = 1
        stop_decel = 0

        ## Axis and encoder parameters
        axis_dir_cw = 0
        encoder_dir_cw = 0

        ## Polarity and enable parameters
        active_low = 0
        active_high = 1
        forward_enable_false = 0
        reverse_enable_false = 0

        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print(f"Model name: {driver_info[0]}, Firmware version: {driver_info[-1]} ")

        ## Define Axis1 ~ Axis3 thread
        thread_1 = threading.Thread(target=Axis1_thread, args=[dev, port, axis1, 0.005])
        thread_2 = threading.Thread(target=Axis2_thread, args=[dev, port, axis2, 0.005])
        thread_3 = threading.Thread(target=Axis3_thread, args=[dev, port, axis3, 0.005])

        ## Thread start
        thread_1.start()
        thread_2.start()
        thread_3.start()

        ## Motion open
        err = await dev.Motion_open_async(port)
        print(f"open_async in port {port}, status: {err}")

        '''
        ## Motion open configuration file
        err = await dev.Motion_openCfgFile_async('C:/Users/user/Desktop/3AxisStage_2P.ini')
        print(f"openCfgFile_async, status: {err}")

        ## Motion load configuration file
        err = await dev.Motion_loadCfgFile_async()
        print(f"loadCfgFile_async, status: {err}")
        '''

        ## Motion configure for axis1
        err = await dev.Motion_cfgAxis_async(port, axis1, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print(f"cfgAxis_async in axis{axis1}, status: {err}")

        err = await dev.Motion_cfgLimit_async(port, axis1, forward_enable_false, reverse_enable_false, active_low)
        print(f"cfgLimit_async in axis{axis1}, status: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis1, encoder_posi=0)
        print(f"rstEncoderPosi_async in axis{axis1}, status: {err}")

        err = await dev.Motion_cfgAxisMove_async(port, axis1, rel_posi_mode, target_posi=1000, velo=10000, accel=100000, decel=100000)
        print(f"cfgAxisMove_async in axis{axis1}, status: {err}")

        ## Servo on
        err = await dev.Motion_enableServoOn_async(port, axis1)
        print(f"ServoOn in axis{axis1}, status: {err}")

        ## Motion configure for axis2
        err = await dev.Motion_cfgAxis_async(port, axis2, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print(f"cfgAxis_async in axis{axis2}, status: {err}")

        err = await dev.Motion_cfgLimit_async(port, axis2, forward_enable_false, reverse_enable_false, active_low)
        print(f"cfgLimit_async in axis{axis2}, status: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis2, encoder_posi=0)
        print(f"rstEncoderPosi_async in axis{axis2}, status: {err}")

        err = await dev.Motion_cfgAxisMove_async(port, axis2, rel_posi_mode, target_posi=1000, velo=10000, accel=100000, decel=100000)
        print(f"cfgAxisMove_async in axis{axis2}, status: {err}")

        ## Servo on
        err = await dev.Motion_enableServoOn_async(port, axis2)
        print(f"ServoOn in axis{axis2}, status: {err}")

        ## Motion configure for axis3
        err = await dev.Motion_cfgAxis_async(port, axis3, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print(f"cfgAxis_async in axis{axis3}, status: {err}")

        err = await dev.Motion_cfgLimit_async(port, axis3, forward_enable_false, reverse_enable_false, active_low)
        print(f"cfgLimit_async in axis{axis3}, status: {err}")

        err = await dev.Motion_rstEncoderPosi_async(port, axis3, encoder_posi=0)
        print(f"rstEncoderPosi_async in axis{axis3}, status: {err}")

        err = await dev.Motion_cfgAxisMove_async(port, axis3, rel_posi_mode, target_posi=-5000, velo=10000, accel=100000, decel=100000)
        print(f"cfgAxisMove_async in axis{axis3}, status: {err}")

        ## Servo on
        err = await dev.Motion_enableServoOn_async(port, axis3)
        print(f"ServoOn in axis{axis3}, status: {err}")

        ## Motion start
        err = await dev.Motion_startMultiAxisMove_async(port, [axis1, axis2, axis3])
        print(f"startMultiAxisMove_async in port {port}, status: {err}")

        ## Wait for thread completion
        thread_1.join()
        print("Axis1_Thread returned.")

        thread_2.join()
        print("Axis2_Thread returned.")

        thread_3.join()
        print("Axis3_Thread returned.")

        ## Servo off
        for i in [axis1, axis2, axis3]:
            err = await dev.Motion_enableServoOff_async(port, i)
            print(f"ServoOff in axis{i}, status: {err}")

        ## Motion stop
        for i in [axis1, axis2, axis3]:
            err = await dev.Motion_stop_async(port, i, stop_decel)
            print(f"stop_async in axis{i}, status: {err}")

        ## Motion close
        err = await dev.Motion_close_async(port)
        print(f"close_async in port {port}, status: {err}")
    except Exception as err:
        pywpc.printGenericError(err)

    finally:
        ## Disconnect device
        dev.disconnect()

        ## Release device handle
        dev.close()


def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))


if __name__ == '__main__':
    asyncio.run(main())  ## Use terminal
    # await main()  ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder()  ## Use Spyder
