# Temperature-TC
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read thermocouple sensor temperature in Celcius.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

In order to run this example, you should get `EthanT` product, which contains thermocouple sensor and its function.

Then, we take `EthanT` for example.

### EthanT

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanT.JPG" alt="drawing" width="600"/>

## Thermocouple Interfacing SOP

Create device handle -> Connect to device -> Open Thermal port -> Set Thermal parameters ->  Read thermocouple data -> Close Thermal port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the EthanT.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.