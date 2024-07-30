# AIO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to do AIO loopback.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### The limitation of the sampling rate.

- For STEM, AO writing can be called while AI is streaming under a specific speed.
- This speed depends on the number of enabled chip-selects.
- Below is the table indicating the max AI sampling rate that allows AO writing.

| CS number  | Sampling rate|
|:----------:|:------------:|
|   3        | 1K           |
|   2        | 1.5K         |
|   1        | 3K           |

### Hardware Requirements

To run this example, you will need a WifiDAQE3AOD product, which contains AI and AO function.

Then, we take `WifiDAQE3AOD` for example.

### WifiDAQE3AOD

- AO0 <-----> AI0, AO1 <-----> AI1, AO2 <-----> AI2, ........, AO6 <-----> AI6, AO7 <-----> AI7

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3AOD.JPG" alt="drawing" width="600"/>

## AIO Interfacing SOP

Create device handle -> Connect to device -> Open AI & AO port -> Write AO signal -> Read AI signal -> Close AI & AO port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the WifiDAQE3AOD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.