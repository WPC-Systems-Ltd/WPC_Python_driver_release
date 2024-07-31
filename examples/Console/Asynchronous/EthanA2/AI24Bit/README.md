# AI24Bit
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AI current value

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a EthanA2 product, which contains AI function.

Here we use EthanA2 as an example.

### EthanA2

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanA2.JPG" alt="drawing" width="600"/>

## Get AI Data

| Product |port | Description      |
|---------|-----|------------------|
| EthanI  | 0   | Get current (mA) |
| EthanIA | 0   | Get current (mA) |
| EthanIA | 1   | Get voltage (V)  |

## AI Interfacing SOP

1. Create device handle
2. Connect to device
3. Open AI port
4. Read AI data on demand
5. Close AI port
6. Disconnect device
7. Release device handle

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)