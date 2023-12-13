# AIO
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to do AIO loopback.

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## How to use this example

### The limitation of the sampling rate.

- For STEM, AO writing can be called while AI is streaming under a specific speed.
- This speed depends on the number of enabled chip-selects.
- Below is the table indicating the max AI sampling rate that allows AO writing.

| CS number  | Sampling rate|
|:----------:|:------------:|
|   3        | 1K           |
|   2        | 1.5K         |
|   1        | 3K           |

### Hardware Requirement

In order to run this example, you should get STEM product, which contains AI and AO function.

Then, we take `STEM` for example.

### STEM

- AO0 <-----> AI0, AO1 <-----> AI1, AO2 <-----> AI2, ........, AO6 <-----> AI6, AO7 <-----> AI7

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-STEM.JPG" alt="drawing" width="600"/>

## AIO interfacing SOP

Create device handle -> Connect to device -> Open AI & AO port -> Write AO signal -> Read AI signal -> Close AI & AO port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `STEM` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.