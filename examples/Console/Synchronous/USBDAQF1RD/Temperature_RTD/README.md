# Temperature-RTD
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read RTD sensor temperature in Celcius.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

In order to run this example, you should get `USBDAQF1RD` product, which contains RTD sensor and its function.

It supports PT100 and PT1000 resistance thermometers, also called resistance temperature detectors (RTDs)

Then, we take `USBDAQF1RD` for example.

### USBDAQF1RD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1RD.JPG" alt="drawing" width="600"/>

## RTD Interfacing SOP

1. Create device handle
2. Connect to device
3. Open thermal port
4. Set thermal parameters
5. Read RTD data
6. Close thermal port
7. Disconnect device
8. Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1RD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.