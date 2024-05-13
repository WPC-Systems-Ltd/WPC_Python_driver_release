# RTC-AI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to use RTC-AI

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

### Hardware Requirement

In order to run this example, you should get EthanA product, which contains RTC-AI function

Then, we take `EthanA` for example.

### EthanA

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanA.JPG" alt="drawing" width="600"/>

## RTC-AI interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Set RTC-AI mode -> Set RTC -> Start RTC alarm -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `EthanA` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.