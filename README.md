## Overview

**WPC Python driver**, also known as `pywpc`, contains APIs for interacting with basically WPC DAQ cards or any other WPC USB, WiFi and Ethernet based devices. It supports Python version from 3.8 to 3.10 under Windows 10 operating systems.

In order to optimize the performance of driver API, we adopt [async/await](https://docs.python.org/3/library/asyncio.html) structure for driver implementation also known as non-blocking method.

Please note, some API functions in the `pywpc` package may not compatible with earlier versions of WPC DAQ firmware. Make sure the latest version of firmware is up to date with your products. To update device firmware to the latest version, please use WPC Device Manager and LabVIEW Run-time engine.
You can download its by [latest release](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/releases/tag/v1.0.2) or visit [WPC Systems Ltd. official website](http://www.wpc.com.tw).

[![pip install](https://img.shields.io/badge/pip%20install-wpcsys-orange.svg)](https://pypi.org/project/wpcsys/)
[![PyPI](https://img.shields.io/pypi/v/wpcsys)](https://pypi.org/project/wpcsys/)
![Python](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10-blue.svg)
![OS](https://img.shields.io/badge/os-Windows%2010-brown.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![docs](https://img.shields.io/badge/docs-passing-green.svg)](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)
![Wheel](https://img.shields.io/pypi/wheel/wpcsys)

|                   |                 Link                                                            |
|:------------------|:--------------------------------------------------------------------------------|
| WPC official site | http://www.wpc.com.tw/                                                          |
| User guide        | https://wpc-systems-ltd.github.io/WPC_Python_driver_release/                    |
| Example code      | https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Examples |

## Quick Start

**Easy, fast, and just works!**

```python
>>> from wpcsys import pywpc

>>> pywpc.PKG_NAME
pywpc

>>> pywpc.__version__
1.0.2

>>> pywpc.product
['DeviceFinder', 'WifiDAQE3A', 'EthanD', 'EthanA', 'USBDAQF1D', 'USBDAQF1AD', 'USBDAQF1DSNK', 'USBDAQF1AOD', 'USBDAQF1TD', 'USBDAQF1CD', 'USBDAQF1RD']

```

## Installation

Install [wpcsys](https://pypi.org/project/wpcsys/) using `pip`:

```
$ pip install wpcsys
```

## Upgrade

Upgrade [wpcsys](https://pypi.org/project/wpcsys/) using `pip`:

```
$ pip install --upgrade wpcsys
```

## Requirements
Python 3.8 or later with all [requirements.txt](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/requirements.txt) dependencies installed, including PyQt5, PyQt5Designer, qasync and so on.

```
$ pip install -r requirements.txt
```

## Products

Ethernet based DAQ card
- Ethan-A
- Ethan-D

USB interface DAQ card
- USB-DAQ-F1-D (Digital)
- USB-DAQ-F1-DSNK (24V Digital)
- USB-DAQ-F1-AD (Digital + AI)
- USB-DAQ-F1-TD (Digital + Thermocouple)
- USB-DAQ-F1-RD (Digital + RTD)
- USB-DAQ-F1-CD (Digital + CAN)
- USB-DAQ-F1-AOD (Digital + AI + AO)

Wifi based DAQ card
- Wifi-DAQ-E3-A

## Port function table

| Model           | AI  | AO | DI         | DO         | CAN | UART | SPI | I2C  | RTD | Thermocouple |
|:----------------|:---:|:--:|:----------:|:----------:|:---:|:----:|:---:|:----:|:---:|:------------:|
| Ethan-A         | 0   | -  | -          | -          |-    |-     |-    |-     | -   |-             |
| Ethan-D         | -   | -  | 1          | 0          |-    |-     |-    |-     | -   |-             |
| USB-DAQ-F1-D    | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |1, 2 | 1, 2 | -   |-             |
| USB-DAQ-F1-DSNK | -   | -  | 0, 1       | 2, 3       |-    |-     |-    |-     | -   |-             |
| USB-DAQ-F1-AD   | 0   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-TD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |1             |
| USB-DAQ-F1-RD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | 1   |-             |
| USB-DAQ-F1-CD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |1    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-AOD  | 0   | 0  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-    | 1, 2 | -   |-             |
| Wifi-DAQ-E3-A   | 1   | -  | -          | -          |-    |-     |-    |-     | -   |-             |

Take `USB-DAQ-F1-AOD` for example:
- Port 0 is available for `AI`
- Port 2 is available for `DI`
- Ports 0 & 1 are available for `DO`
- Port 2 is available for `UART`

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
