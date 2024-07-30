# AI
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AI current value

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a EthanIA product, which contains AI function.

Here we use EthanIA as an example.

### EthanIA

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanIA.JPG" alt="drawing" width="600"/>

## Get AI data

| Product |port | Description      |
|---------|-----|------------------|
| EthanI  | 0   | Get current (mA) |
| EthanIA | 0   | Get current (mA) |
| EthanIA | 1   | Get voltage (V)  |

## AI Interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the EthanIA.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.