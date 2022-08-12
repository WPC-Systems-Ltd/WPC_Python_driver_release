import sys
import asyncio
sys.path.append('src/')
# sys.path.append('build/')
# sys.path.append('pywpc/')
import pywpc

async def loop_onDemand(handle, delay = 1):
    while True:
        data =  await handle.readAIOnDemand()
        print("data :" + str(data))
        await asyncio.sleep(delay)

async def loop_wifiSystem(handle, delay = 1):
    while True:
        task_fct_list = [handle.readRSSI(), handle.readThermo(), handle.readBattery()]
        res_list = await asyncio.gather(*task_fct_list)
        print("Rssi: "+ str(res_list[0]) + " dBm")
        print("Thermo: "+ str(res_list[1]) + " °C")
        print("Battery: "+ str(res_list[2]) + " mV")
        await asyncio.sleep(delay)

async def main():

    print("Start example code...")
    ## Get python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create handle
    dev = pywpc.WifiDAQE3A() 

    ## Connect
    try:
        dev.connect("192.168.5.79") ## Put web device's IP here
    except Exception as err:
        pywpc.printGenericError(err)

    ## Execute
    try:
        # state = await dev.setRTCDateTime("2022/10/12, 18:02:58")
        state = await dev.sys_setRTC(2022,10,12,18,2,58)
        print(state)

        time_ = await dev.sys_getRTC()
        print(time_)
        # await asyncio.gather(loop_onDemand(dev, 1), loop_wifiSystem(dev, 3))
    except Exception as err:
        pywpc.printGenericError(err)

    dev.disconnect()
    dev.close()
    print("End example code...")

    return

if __name__ == '__main__':
    asyncio.run(main())
