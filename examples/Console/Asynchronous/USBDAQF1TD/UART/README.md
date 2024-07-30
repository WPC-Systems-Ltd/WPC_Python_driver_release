# UART
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write through UART interface.

In order to verify, please take another WPC USB DAQ device or other device which support UART interface.

We connect two device via UART so that can communicate data.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1TD product, which contains UART function.

Then, we take `USBDAQF1TD` for example.

### USBDAQF1TD

|   Model name     | port  | RX   | TX   |
| -----------------|:-----:|:----:|:----:|
| USBDAQF1TD       | UART2 | P1.2 | P1.3 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>

## UART Interfacing SOP

Create device handle -> Connect to device -> Open UART port -> Set UART parameters -> Write data via UART -> Read data via UART -> Close UART port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1TD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.