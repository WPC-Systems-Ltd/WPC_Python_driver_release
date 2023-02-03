# UART
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write through UART interface.

In order to verify, please take another WPC USB DAQ device or other device which support UART interface.

We connect two device via UART so that can communicate data.
 
In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own UART application (for example, read the temperature data from external sensor with UART interface), try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get USBDAQF1RD product, which contains UART function. 

Then, we take `USBDAQF1RD` for example.

### USBDAQF1RD

|   Model name     | port  | RX   | TX   |
| -----------------|:-----:|:----:|:----:|
| USBDAQF1RD   | UART2 | P1.2 | P1.3 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1RD.JPG" alt="drawing" width="600"/>

## UART interfacing SOP 

Create device handle -> Connect to device -> Open UART port -> Set UART parameters -> Write data via UART -> Read data via UART -> Close UART port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `USBDAQF1RD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.