'''
AO - AO_waveform_gen.py with asynchronous mode.

This example demonstrates the process of writing AO signal of STEM.
To begin with, it demonstrates the steps to open AO and configure the AO parameters.
Next, it outlines the procedure for AO streaming.
Finally, it concludes by explaining how to close AO.

If your product is "STEM", please invoke the function `Sys_setAIOMode_async`.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## Python
import asyncio

## WPC

from wpcsys import pywpc


async def main():
    ## STEM has not supported yet

def main_for_spyder(*args):
    if asyncio.get_event_loop().is_running():
        return asyncio.create_task(main(*args)).result()
    else:
        return asyncio.run(main(*args))
if __name__ == '__main__':
    asyncio.run(main()) ## Use terminal
    # await main() ## Use Jupyter or IPython(>=7.0)
    # main_for_spyder() ## Use Spyder