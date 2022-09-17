## About

**WPC Python device driver** contains APIs for interacting with the WPC USB-DAQ, Ethernet and Wifi-DAQ series products.

In order to optimize driver API performance, we adopt [async/await](https://docs.python.org/3/library/asyncio.html) structure for the driver implementation as known as non-blocking mode. 

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
WPC Python device driver

>>> pywpc.__version__
...
0.2.2

>>> dev.connect()
...
Binded Device finder

>>> await dev.Bcst_getDeviceInfo()
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

- [Python](https://www.python.org) \>= 3.10
- [PyQt5](https://pypi.org/project/PyQt5/)(tested to work with\>=5.15.7)
- [matplotlib](https://matplotlib.org/) \>= 3.5.2
- [Numpy](http://www.numpy.org)(tested to work with\>=1.23.0)
- [pyusb](https://pypi.org/project/pyusb/) \>= 1.2.1
- [qasync](https://pypi.org/project/qasync/) \>= 0.23.0
- [wpcEXEbuild](https://pypi.org/project/wpcEXEbuild/) \>= 0.0.1

## Products
 
WiFi based DAQ card
- Wifi-DAQ-E3-A

Ethernet based remote controller
- STEM (unsupported)
- STEM-Lite (unsupported)

Ethernet based motion card
- EMotion (unsupported)

Ethernet based DAQ card
- EPC (unsupported)
- Ethan-D
- Ethan-A

USB interface DAQ card
- USB-DAQ-F1-D
- USB-DAQ-F1-AD
- USB-DAQ-F1-TD
- USB-DAQ-F1-RD
- USB-DAQ-F1-CD
- USB-DAQ-F1-AOD
- USB-DAQ-F1-DSNK

## Port funtion table

| Model           | AI  | AO | DI         | DO         | CAN | UART | SPI | I2C  | RTD | Thermocouple |
|:----------------|:---:|:--:|:----------:|:----------:|:---:|:----:|:---:|:----:|:---:|:------------:|
| Wifi-DAQ-E3-A   | 1   | -  | -          | -          |-    |-     |-    |-     | -   |-             |
| Ethan-D         | -   | -  | 1          | 0          |-    |-     |-    |-     | -   |-             |
| Ethan-A         | 0   | -  | -          | -          |-    |-     |-    |-     | -   |-             |
| USB-DAQ-F1-DSNK | -   | -  | 0, 1       | 2, 3       |-    |-     |-    |-     | -   |-             |
| USB-DAQ-F1-AOD  | 0   | 0  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-    | 1, 2 | -   |-             |
| USB-DAQ-F1-AD   | 0   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-D    | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |1, 2 | 1, 2 | -   |-             |
| USB-DAQ-F1-TD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | -   |1             |
| USB-DAQ-F1-CD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |1    |1, 2  |2    | 1, 2 | -   |-             |
| USB-DAQ-F1-RD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |2    | 1, 2 | 1   |-             |

Take `USB-DAQ-F1-AOD` for example
- port0 is available for `AI`
- port2 is available for `DI`
- port0 and port1 are available for `DO`
- port2 is available for `UART`

## References

- [User manual - WPC Python device driver](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)
- [Recommendations for new python user to create environment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment) 
- [Run example code in console](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console)
- [How to build your own Python code to EXE file](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-build-your-own-Python-code-to-EXE-file)

## License

**WPC Python device driver** is licensed under an MIT-style license see
[LICENSE](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE). Other incorporated projects may be licensed under different licenses.

All licenses allow for non-commercial and commercial use.
