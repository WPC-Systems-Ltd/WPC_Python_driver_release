# AI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire multi-channel AI data simultaneously.
Also, we show how to perform data acquisition in on-demand, N samples and continuous mode individually.

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## Sampling rate

### The sampling rate is dependent on the channel.

| Product/channel | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|:---------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| USB-DAQ-F1-AD   | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|
| USB-DAQ-F1-AOD  | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|

### The sampling rate is dependent on the chip select.

| Product/CS  | 1  | 2  |3   |
|:-----------:|:--:|:--:|:--:|
| STEM        |12k |6k  |4k  |

### The sampling rate is independent.

| Product     |Sampling rate|
|:-----------:|:-----------:|
| Wifi-DAQ    | 10k         |
| Ethan-A     | 20k         |

### Hardware requirement

In order to run this example, you should get EthanA product, which contains AI function.

Then, we take EthanA for example.

### EthanA

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanA.JPG" alt="drawing" width="600"/>

## AI interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `EthanA` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.