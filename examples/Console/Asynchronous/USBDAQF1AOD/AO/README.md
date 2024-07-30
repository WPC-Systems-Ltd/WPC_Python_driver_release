# AO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to output digital signal.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### AO output range

| Product         |AO range    |
|:---------------:|:----------:|
| USB-DAQ-F1-AOD  | 0 ~ 5 V    |
| Ethan-O         | -10 ~ 10 V |
| STEM            | -10 ~ 10 V |

### Hardware Requirements

To run this example, you will need a USBDAQF1AOD product, which contains AO function.

Then, we take `USBDAQF1AOD` for example.

### USBDAQF1AOD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1AOD.JPG" alt="drawing" width="600"/>

## AO Interfacing SOP

Create device handle -> Connect to device -> Open AO port -> Write AO signal -> Close AO port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1AOD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.