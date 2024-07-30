# DIO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to control DIO with whole port or assign pins

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1D product, which contains DIO function.

Then, we take `USBDAQF1D` for example.

### USBDAQF1D

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1D.JPG" alt="drawing" width="600"/>

## DO Interfacing SOP

1. Create device handle
2. Connect to device
3. Open DO port/pins
4. Write high or low value
5. Close DO port/pins
6. Disconnect device
7. Release device handle.

## DI Interfacing SOP
1. Create device handle
2. Connect to device
3. Open DI port/pins
4. Read high or low value
5. Close DI port/pins
6. Disconnect device
7. Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1D.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.