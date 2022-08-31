## Overview

This example project demonstrates how to use WPC python driver to do AIO loopback.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AIO application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get one of WPC-USB-DAQ-F1-AOD which contain AI and AO function.

Then, we take `WPC-USB-DAQ-F1-AOD` for example.

### WPC-USB-DAQ-F1-AOD

- AO0 <-----> AI0, AO1 <-----> AI1, AO2 <-----> AI2, ........, AO6 <-----> AI6, AO7 <-----> AI7

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-AOD.JPG" alt="drawing" width="600"/>

## AIO interfacing SOP 

Create device handle -> Connect to device -> Open AI & AO port -> Write AO signal -> Read AI signal -> Close AI & AO port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-AOD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.