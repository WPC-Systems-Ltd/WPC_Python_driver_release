# DPOT
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read/write digital potentiometer resistance.

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get EthanP product, which contains DPOT function.

Then, we take `EthanP` for example.

### EthanP

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanP.JPG" alt="drawing" width="600"/>

## DPOT interfacing SOP

# DPOT
Create device handle -> Connect to device -> Open DPOT -> Read/Write digital potentiometer resistance-> Close DPOT -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `EthanP` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.