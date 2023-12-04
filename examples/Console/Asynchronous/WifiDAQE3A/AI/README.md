# AI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire multi-channel AI data simultaneously.
Also, we show how to perform data acquisition in on-demand, N samples and continuous mode individually.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AI application, try to use this as a basic template, then add your own code.

## How to use this example

### Channel count vs. sampling rate

| Product/module  |chan 0:0|chan 0:1|chan 0:2|chan 0:3|chan 0:4|chan 0:5|chan 0:6|chan 0:7|
|:---------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| USB-DAQ-F1-AD   | 20k    | 12.5k  | 8.1k   | 6.3k   | 4k     | 3.2k   | 3.2k   | 2.5k   |
| USB-DAQ-F1-AOD  | 20k    | 12.5k  | 8.1k   | 6.3k   | 4k     | 3.2k   | 3.2k   | 2.5k   |
| Wifi-DAQ        | 10k    | 10k    | 10k    | 10k    | 10k    | 10k    | 10k    | 10k    |
| Ethan-A         | 20k    | 20k    | 20k    | 20k    | 20k    | 20k    | 20k    | 20k    |

### Hardware requirement

In order to run this example, you should get WifiDAQE3A product, which contains AI function.

Then, we take WifiDAQE3A for example.

### WifiDAQE3A

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3A.JPG" alt="drawing" width="600"/>

## AI interfacing SOP

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WifiDAQE3A` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.