## Overview

This example project demonstrates how to use WPC python driver to output digital signal.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AO application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get one of WPC-USB-DAQ-F1-AOD which contain AO function.

Then, we take `WPC-USB-DAQ-F1-AOD` for example.

### WPC-USB-DAQ-F1-AOD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-AOD.JPG" alt="drawing" width="600"/>

## AO interfacing SOP 

Create device handle -> Connect to device -> Open AO port -> Write AO signal -> Close AO port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-AOD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.