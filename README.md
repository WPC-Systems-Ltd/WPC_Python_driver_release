 
## WPC_Device_Driver_Example_GUI
 
WPC driver only support python 3.10

## Python version requirement
- Python 3.10 

Products
--------
Wifi DAQ:
- Wifi-DAQ-E3-A

Ethernet controller:
- STEM
- STEM-Lite

Ethernet motion card
- EMotion

Ethernet DAQ
- EPC
- Ethan-D
- Ethan-A

USB DAQ
- USB-DAQ-F1-D
- USB-DAQ-F1-AD
- USB-DAQ-F1-TD
- USB-DAQ-F1-CD
- USB-DAQ-F1-AOD
- USB-DAQ-F1-DSNK

Port configurations
-------------------

| Board           | AI  | AO | DI         | DO         | CAN | UART |ThermoCouple|
|:----------------|:---:|:--:|:----------:|:----------:|:---:|:----:|:----------:|
| Wifi-DAQ-E3-A   | 1   | -  | -          | -          |-    |-     |-           |
| Ethan-D         | -   | -  | 1          | 0          |-    |-     |-           |
| Ethan-A         | 0   | -  | -          | -          |-    |-     |-           |
| USB-DAQ-F1-DSNK | -   | -  | 0, 1       | 2, 3       |-    |-     |-           |
| USB-DAQ-F1-AOD  | 0   | 0  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-           |
| USB-DAQ-F1-AD   | 0   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-           |
| USB-DAQ-F1-D    | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |-           |
| USB-DAQ-F1-TD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |1           |
| USB-DAQ-F1-CD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |1    |1, 2  |-           |
| USB-DAQ-F1-RD   | -   | -  | 0, 1, 2, 3 | 0, 1, 2, 3 |-    |1, 2  |1           |


## Reference
- [User manual](https://wpc-systems.github.io/WPC_Python_driver_release/)
- [Recommend for new python user to create environment](https://github.com/WPC-systems/WPC_Python_driver_release/wiki/Install-miniconda-and-build-environment) 
- [Run example code in console](https://github.com/WPC-systems/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console)

