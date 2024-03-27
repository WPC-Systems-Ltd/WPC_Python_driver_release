# AI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AI current value

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## How to use this example

### Hardware requirement

In order to run this example, you should get EthanI product, which contains AI function.

Then, we take EthanI for example.

### EthanI

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanI.JPG" alt="drawing" width="600"/>

## Get AI data

| Product |port | Description      |
|---------|-----|------------------|
| EthanI  | 0   | Get current (mA) |
| EthanIA | 0   | Get current (mA) |
| EthanIA | 1   | Get voltage (V)  |

## AI interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `EthanI` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.