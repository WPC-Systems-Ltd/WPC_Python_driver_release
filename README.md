 
## WPC Device Driver Example GUI
 
- WPC device driver only support python 3.10

## Python version requirement
- Python 3.10 

Products
--------
WiFi based DAQ card
- Wifi-DAQ-E3-A

Ethernet based remote controller
- STEM
- STEM-Lite

Ethernet based motion card
- EMotion

Ethernet based DAQ card
- EPC
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

Port funtion table
------------------

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
- port0 & port1 are available for `DO`
- port2 is available for `UART`

## References
- [User manual - WPC Python Device Driver](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)
- [Recommendations for new python user to create environment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment) 
- [Run example code in console](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console)

License
=======

**WPC Python driver** is licensed under an MIT-style license (see
`LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
