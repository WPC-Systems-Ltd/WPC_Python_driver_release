## Overview

**WPC Python driver** is also known as `pywpc` which contains APIs for interacting with the WPC USB-DAQ, Ethernet and Wifi-DAQ series products. It supports Python 3.8 to 3.10 in Windows 10 operating systems.

In order to optimize driver API performance, we adopt [async/await](https://docs.python.org/3/library/asyncio.html) structure for the driver implementation as known as non-blocking mode.

Some functions in the `pywpc` package may be unavailable with earlier versions of the WPC DAQ firmware driver. Make sure it's the latest firmware version of your product. Please visit WPC Systems offical website to download [WPC Device Manager and LabVIEW Run-time engine
](http://www.wpc.com.tw/36039260092584721462-daq1.html) and upgrade WPC DAQ firmware driver.


[![pip install](https://img.shields.io/badge/pip%20install-wpcsys-orange.svg)](https://pypi.org/project/wpcsys/)
[![PyPI](https://img.shields.io/pypi/v/wpcsys)](https://pypi.org/project/wpcsys/)
![Python](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10-blue.svg)
![OS](https://img.shields.io/badge/os-Windows%2010-brown.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![docs](https://img.shields.io/badge/docs-passing-green.svg)](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)
![Wheel](https://img.shields.io/pypi/wheel/wpcsys)

|                  |                 Link                                                            |
|:-----------------|:-------------------------------------------------------------------------------:|
| WPC Systems Ltd  | http://www.wpc.com.tw/                                                          |
| Documentation    | https://wpc-systems-ltd.github.io/WPC_Python_driver_release/                    |
| Example code     | https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples | 



## Quick Start

In the bellowing example, we use **pywpc** to find all available WPC devices.

**pywpc.pyd** is a Python based dll file which support on win10 x64.

```python
>>> from wpcsys import pywpc

>>> dev = pywpc.Broadcaster()
...
Opened handle (Device finder)
 
>>> pywpc.PKG_FULL_NAME
...
WPC Python driver

>>> dev.connect()
...
Binded Device finder

>>> await dev.Bcst_getDeviceInfo_async()
...
[['192.168.5.79', '255.255.255.0', '34:86:5d:19:06:6c', 'Wifi-DAQ-E3-A_R0.3.4']]

>>> dev.disconnect()
...
Disconnected Device finder

>>> dev.close()
...
Closed handle (Device finder)
```

## Installation

Install [wpcsys](https://pypi.org/project/wpcsys/) using `pip`:

```
$ pip install wpcsys
```

## Upgrade

Upgrade `wpcsys` using `pip`:


```
$ pip install --upgrade wpcsys
```

## Requirements
- [Python](https://www.python.org) \>= 3.8 
- [PyQt5](https://pypi.org/project/PyQt5/) (has been tested \>=5.15.4)
- [PyQt5Designer](https://pypi.org/project/PyQt5Designer/) \>= 5.14.1
- [PyQt5-Qt5](https://pypi.org/project/PyQt5-Qt5/) \>= 5.15.2
- [PyQt5-sip](https://pypi.org/project/PyQt5-sip/) \>= 12.10.1
- [qasync](https://pypi.org/project/qasync/) \>= 0.23.0
- [matplotlib](https://matplotlib.org/) \>= 3.5.2
- [Numpy](http://www.numpy.org) (has been tested \>=1.23.0)
- [pyusb](https://pypi.org/project/pyusb/) \>= 1.2.1 
- [wpcEXEbuild](https://pypi.org/project/wpcEXEbuild/) \>= 0.0.1

## Products
 
Wifi based DAQ card
- Wifi-DAQ-E3-A

Ethernet based DAQ card
- Ethan-A
- Ethan-D
 
USB interface DAQ card
- USB-DAQ-F1-D
- USB-DAQ-F1-AD
- USB-DAQ-F1-CD
- USB-DAQ-F1-TD
- USB-DAQ-F1-RD 
- USB-DAQ-F1-AOD
- USB-DAQ-F1-DSNK

## Port funtion table

| Model           | AI  | AO | DI         | DO         | CAN | UART | SPI | I2C  | RTD | Thermocouple |
|:---------------:|:---:|:--:|:----------:|:----------:|:---:|:----:|:---:|:----:|:---:|:------------:|
| Wifi-DAQ-E3-A   | 1   | -  | -          | -          |-    |-     |-    |-     | -   |-             |
| Ethan-A         | 0   | -  | -          | -          |-    |-     |-    |-     | -   |-             |
| Ethan-D         | -   | -  | 1          | 0          |-    |-     |-    |-     | -   |-             |
| USB-DAQ-F1-D    | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |1, 2 | 1, 2 | -   |-             |
| USB-DAQ-F1-AD   | 0   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-CD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |1    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-TD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |1             |
| USB-DAQ-F1-RD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | 1   |-             |
| USB-DAQ-F1-AOD  | 0   | 0  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-    | 1, 2 | -   |-             |
| USB-DAQ-F1-DSNK | -   | -  | 0, 1       | 2, 3       |-    |-     |-    |-     | -   |-             |

Take `USB-DAQ-F1-AOD` for example
- port0 is available for `AI`
- port2 is available for `DI`
- port0 and port1 are available for `DO`
- port2 is available for `UART`

## References

- [Useful conda commands](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/Useful-Conda-Commands)
- [User manual - WPC Python driver](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)
- [Run example code in console](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console)
- [How to build your own Python code to EXE file](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-build-your-own-Python-code-to-EXE-file)
- [How to install miniconda and build your own virtual environment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment) 

## License

**WPC Python driver release** is licensed under an MIT-style license see
[LICENSE](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE). Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.
