# AI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AHRS data.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own AHRS application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware requirement

In order to run this example, you should get WifiDAQE3A product, which contains AHRS function.

Then, we take WifiDAQE3A for example.

### WifiDAQE3A

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3A.JPG" alt="drawing" width="600"/>

## AHRS interfacing SOP

Create device handle -> Connect to device -> Open AHRS port -> Read AHRS data -> Close AHRS port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WifiDAQE3A` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.