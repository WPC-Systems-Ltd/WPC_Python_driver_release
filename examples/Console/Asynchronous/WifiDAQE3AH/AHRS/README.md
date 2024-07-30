# AHRS
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AHRS data.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a WifiDAQE3AH product, which contains AHRS function.

Here we use WifiDAQE3AH as an example.

### WifiDAQE3AH

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3AH.JPG" alt="drawing" width="600"/>

## Get AHRS's estimation with mode.

| Mode |  Description                                                   |
|------|----------------------------------------------------------------|
|   0  | 3-axis of orientation                                          |
|   1  | 3-axis of acceleration                                         |
|   2  | 3-axis of angular velocity                                     |
|   3  | 3-axis of orientation and acceleration                         |
|   4  | 3-axis of orientation and angular velocity                     |
|   5  | 3-axis of angular velocity and acceleration                    |
|   6  | 3-axis of orientation and angular velocity and acceleration    |

## AHRS Interfacing SOP

Create device handle -> Connect to device -> Open AHRS port -> Read AHRS data -> Close AHRS port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the WifiDAQE3AH.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.