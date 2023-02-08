'''
Motion - Motion_3axis_asynchronous_move.py with asynchronous mode.
 
For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd.
All rights reserved.
'''

## Python
import threading
import time
import asyncio

## WPC

from wpcsys import pywpc


async def getAxisStatus(handle, port, axis, delay = 0.005):
    move_status = await handle.Motion_getMoveStatus_async(port, axis)
    if move_status != 0:
        print(f"Move completed axis {axis}...") 
    await asyncio.sleep(delay)  ## delay(second)
    return move_status

def Axis1_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))
        time.sleep(delay)

def Axis2_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))
        time.sleep(delay)

def Axis3_thread(handle, port, axis, delay = 0.005):
    move_status = 0
    while move_status == 0:
        move_status = asyncio.run(getAxisStatus(handle, port, axis, delay))
        time.sleep(delay) 
    
async def main():
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
        ## Get firmware model & version
        driver_info = await dev.Sys_getDriverInfo_async()
        print("Model name:" + driver_info[0])
        print("Firmware version:" + driver_info[-1])

        ## Parameters setting
        port = 0
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

        ## Define Axis1 ~ Axis3 thread
        thread_1 = threading.Thread(target = Axis1_thread, args=[dev, port, axis1, 0.005]) 
        thread_2 = threading.Thread(target = Axis2_thread, args=[dev, port, axis2, 0.005]) 
        thread_3 = threading.Thread(target = Axis3_thread, args=[dev, port, axis3, 0.005])

        ## Thread start
        thread_1.start()
        thread_2.start()
        thread_3.start()

        ## Motion open
        err = await dev.Motion_open_async(port)
        print("open_async:", err)

        ## Motion configure for axis1
        err = await dev.Motion_cfgAxis_async(port, axis1, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print("cfgAxis_async axis1:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis1, forward_enable_false, reverse_enable_false, active_low)
        print("cfgLimit_async axis1:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis1)
        print("rstEncoderPosi_async axis1:", err)

        err = await dev.Motion_cfgAxisMove_async(port, axis1, rel_posi_mode, target_position = 1000)
        print("cfgAxisMove_async axis1:", err)

        err = await dev.Motion_enableServoOn_async(port, axis1, int(True))
        print("enableServoOn_async axis1:", err)

        ## Motion start for axis1
        err = await dev.Motion_startSingleAxisMove_async(port, axis1)
        print("startSingleAxisMove_async axis1:", err)

        ## Motion configure for axis2
        err = await dev.Motion_cfgAxis_async(port, axis2, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print("cfgAxis_async axis2:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis2, forward_enable_false, reverse_enable_false, active_low)
        print("cfgLimit_async axis2:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis2)
        print("rstEncoderPosi_async axis2:", err)

        err = await dev.Motion_cfgAxisMove_async(port, axis2, rel_posi_mode, target_position = 1000)
        print("cfgAxisMove_async axis2:", err)

        err = await dev.Motion_enableServoOn_async(port, axis2, int(True))
        print("enableServoOn_async axis2:", err)

        ## Motion start for axis2
        err = await dev.Motion_startSingleAxisMove_async(port, axis2)
        print("startSingleAxisMove_async axis2:", err)

        ## Motion configure for axis3
        err = await dev.Motion_cfgAxis_async(port, axis3, two_pulse_mode, axis_dir_cw, encoder_dir_cw, active_low)
        print("cfgAxis_async axis3:", err)
            
        err = await dev.Motion_cfgLimit_async(port, axis3, forward_enable_false, reverse_enable_false, active_low)
        print("cfgLimit_async axis3:", err)

        err = await dev.Motion_rstEncoderPosi_async(port, axis3)
        print("rstEncoderPosi_async axis3:", err)

        err = await dev.Motion_cfgAxisMove_async(port, axis3, rel_posi_mode, target_position = -5000)
        print("cfgAxisMove_async axis3:", err)

        err = await dev.Motion_enableServoOn_async(port, axis3, int(True))
        print("enableServoOn_async axis3:", err)

        ## Motion start for axis3
        err = await dev.Motion_startSingleAxisMove_async(port, axis3)
        print("startSingleAxisMove_async axis3:", err)
        
        ## Wait for thread completion
        thread_1.join()
        print("Axis1_Thread returned.")

        thread_2.join()
        print("Axis2_Thread returned.")

        thread_3.join() 
        print("Axis3_Thread returned.")
    
        for i in [axis1, axis2, axis3]:
            err = await dev.Motion_enableServoOn_async(port, i, int(False))
            print(f"enableServoOn_async axis{i} :", err) 
  
        ## Motion stop
        for i in [axis1, axis2, axis3]:
            err = await dev.Motion_stop_async(port, i, stop_decel)
            print(f"stop_async axis{i} :", err) 
 
        ## Motion close
        err = await dev.Motion_close_async(port)
        print("close_async:", err) 
    except Exception as err:
        pywpc.printGenericError(err)

    ## Disconnect device
    dev.disconnect()

    ## Release device handle
    dev.close()
 
    return

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))
 
if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder