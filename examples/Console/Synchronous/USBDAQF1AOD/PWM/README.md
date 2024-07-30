# PWM
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver with PWM

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own PWM application, try to use this as a basic template, then add your own code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1AOD product, which contains PWM function.

Then, we take `USBDAQF1AOD` for example.

### USBDAQF1AOD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1AOD.JPG" alt="drawing" width="600"/>

## PWM Interfacing SOP

1. Create device handle
2. Connect to device
3. Open PWM
4. Set PWM parameters
5. Start PWM
6. Stop PWM
7. Close PWM
8. Disconnect device
9. Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1AOD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.