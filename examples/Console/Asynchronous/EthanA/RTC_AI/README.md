# RTC-AI
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to use RTC-AI

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

### Hardware Requirements

To run this example, you will need a EthanA product, which contains RTC-AI function

Then, we take `EthanA` for example.

### EthanA

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanA.JPG" alt="drawing" width="600"/>

## RTC-AI Interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Set AI mode -> Set AI trigger mode -> Set RTC -> Start RTC alarm -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the EthanA.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.