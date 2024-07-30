# AI
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire multi-channel AI data simultaneously.
Also, we show how to perform data acquisition in on-demand, N samples and continuous mode individually.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Sampling rate

#### The max sampling rate is dependent on the number of enabled channels.

| Product/channel | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|:---------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| USB-DAQ-F1-AD   | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|
| USB-DAQ-F1-AOD  | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|

#### The max sampling rate is dependent on the number of enabled chip-selects.

| Product/CS  | 1  | 2  |3   |
|:-----------:|:--:|:--:|:--:|
| STEM        |12k |6k  |4k  |

#### The max sampling rate is fixed.

| Product         |Sampling rate|
|:---------------:|:-----------:|
| Wifi-DAQ-E3-A   | 10k         |
| Wifi-DAQ-E3-AH  | 10k         |
| Wifi-DAQ-E3-AOD | 10k         |
| Wifi-DAQ-F4-A   | 20k         |
| Ethan-A         | 20k         |
| Ethan-A2        | 10k         |

### Hardware Requirements

To run this example, you will need a USBDAQF1AD product, which contains AI function.

Here we use USBDAQF1AD as an example.

### USBDAQF1AD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1AD.JPG" alt="drawing" width="600"/>

## AI Interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Configure AI -> Open AI streaming -> Read AI streaming -> Close AI streaming -> Close AI port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1AD.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.