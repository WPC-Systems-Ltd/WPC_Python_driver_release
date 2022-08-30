## Overview

This project example code demonstrate how to use WPC python driver to get AI data with 8 channels simultaneously.
Also, we demonstrate how to use AI Continuous, N samples and on demand mode to get data correctly.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AI application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should have one of WPC-USB-DAQ-F1-AD, Ethan-A and WPC-Wifi-DAQ-E3-A, those contain AI components.

Then, we take `WPC-Wifi-DAQ-E3-A` for example.

### WPC-Wifi-DAQ-E3-A

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/Wifi-DAQ-E3-A.JPG" alt="drawing" width="600"/>

## AI interfacing SOP 

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-Wifi-DAQ-E3-A` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.