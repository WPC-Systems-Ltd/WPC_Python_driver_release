# Counter
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver with counter

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own counter application, try to use this as a basic template, then add your own code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1D product, which contains counter function.

Then, we take `USBDAQF1D` for example.

### USBDAQF1D

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1D.JPG" alt="drawing" width="600"/>

## Counter Interfacing SOP

1. Create device handle
2. Connect to device
3. Open counter
4. Set counter parameters
5. Start counter
5. Read counter position
6. Stop counter
7. Close counter
8. Disconnect device
9. Release device handle

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)