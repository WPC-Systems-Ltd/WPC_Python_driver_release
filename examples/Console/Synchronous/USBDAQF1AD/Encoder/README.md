# Encoder
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver with encoder

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own encoder application, try to use this as a basic template, then add your own code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1AD product, which contains encoder function.

Then, we take `USBDAQF1AD` for example.

### USBDAQF1AD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1AD.JPG" alt="drawing" width="600"/>

## Encoder Interfacing SOP

1. Create device handle
2. Connect to device
3. Open encoder
4. Set encoder parameters
5. Start encoder
6. Read encoder
7. Stop encoder
8. Close encoder
9. Disconnect device
10. Release device handle

A return value of 0 indicates successful communication with the USBDAQF1AD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.