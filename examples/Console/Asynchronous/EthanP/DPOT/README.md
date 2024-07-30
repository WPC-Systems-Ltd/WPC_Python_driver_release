# DPOT
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read/write digital potentiometer resistance.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a EthanP product, which contains DPOT function.

Then, we take `EthanP` for example.

### EthanP

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanP.JPG" alt="drawing" width="600"/>

## DPOT Interfacing SOP

# DPOT
Create device handle -> Connect to device -> Open DPOT -> Read/Write digital potentiometer resistance-> Close DPOT -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the EthanP.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.