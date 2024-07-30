# AIO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to do AIO loopback.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### The Limitation Of The Sampling Rate.

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

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3AOD.JPG" alt="drawing" width="600"/>

## AIO Interfacing SOP

1. Create device handle
2. Connect to device
3. Open AI & AO port
4. Configure AI & AO
5. Write AO signal
6  Read AI on demand (Depends)
7. Open AI streaming (Depends)
8. Start AI streaming (Depends)
9 Read AI streaming (Depends)
10. Close AI streaming (Depends)
11. Close AI & AO port
12. Disconnect device
13. Release device handle.

A return value of 0 indicates successful communication with the WifiDAQE3AOD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.