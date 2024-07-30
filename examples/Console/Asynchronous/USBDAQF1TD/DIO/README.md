# DIO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to control DIO with whole port or assign pins

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1TD product, which contains DIO function.

Then, we take `USBDAQF1TD` for example.

### USBDAQF1TD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>

## DIO Interfacing SOP

# DO
Create device handle -> Connect to device -> Open DO port / pins -> Write high or low to digital output -> Close DO port / pins -> Disconnect device -> Release device handle.

# DI
Create device handle -> Connect to device -> Open DI port / pins -> Read high or low from digital input -> Close DI port / pins -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1TD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.