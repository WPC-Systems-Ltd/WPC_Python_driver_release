# UART
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write through UART interface.

In order to verify, please take another WPC USB DAQ device or other device which support UART interface.

We connect two device via UART so that can communicate data.

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get USBDAQF1D product, which contains UART function.

Then, we take `USBDAQF1D` for example.

### USBDAQF1D

|   Model name     | port  | RX   | TX   |
| -----------------|:-----:|:----:|:----:|
| USBDAQF1D       | UART2 | P1.2 | P1.3 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1D.JPG" alt="drawing" width="600"/>

## UART interfacing SOP

Create device handle -> Connect to device -> Open UART port -> Set UART parameters -> Write data via UART -> Read data via UART -> Close UART port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `USBDAQF1D` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.