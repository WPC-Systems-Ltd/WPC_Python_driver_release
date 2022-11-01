
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire multi-channel AI data simultaneously.
Also, we show how to perform data acquisition in on-demand, N samples and continuous mode individually.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AI application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get EthanA product, which contains AI function.

Then, we take EthanA for example.

### EthanA

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/EthanA.JPG" alt="drawing" width="600"/>

## AI interfacing SOP 

Create device handle -> Connect to device -> Open AI port -> Read AI data -> Close AI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `EthanA` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.