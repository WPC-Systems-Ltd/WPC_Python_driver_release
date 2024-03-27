# AHRS
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC Python driver to acquire AHRS data.

In order to use API correctly, please refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you'd like to create your own application, start by using this simple template, and then include your own code.

## How to use this example

### Hardware requirement

In order to run this example, you should get WifiDAQE3AH product, which contains AHRS function.

Then, we take WifiDAQE3AH for example.

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

## AHRS interfacing SOP

Create device handle -> Connect to device -> Open AHRS port -> Read AHRS data -> Close AHRS port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WifiDAQE3AH` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.