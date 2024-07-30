# CAN
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write through CAN interface.

In order to verify, please take another `USBDAQF1CD` or other device which support CAN interface.
We connect two device via CAN so that can communicate data.

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

In order to verify, please get two USBDAQF1CD products or one with any other device which support CAN interface.

Then, we take `USBDAQF1CD` for example.

### USBDAQF1CD

Both connect CAN_H to CAN_H and CAN_L to CAN_L then short pin35, pin36 together for enabling termination resistor.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1CD.JPG" alt="drawing" width="600"/>

## CAN Interfacing SOP

1. Create device handle
2. Connect to device
3. Open CAN port
4. Set CAN parameters
5. Write data via CAN
6. Read data via CAN
7. Close CAN port
8. Disconnect device
7. Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1CD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.