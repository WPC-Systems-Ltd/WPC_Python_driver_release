
> **Note**
> Make sure you are connected to correct IP or serial number.

# Temperature-TC

## Overview

This example project demonstrates how to use WPC python driver to read thermocouple sensor temperature in Celcius.

If you want to build your own thermocouple application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get `USBDAQF1TD` product, which contains thermocouple sensor and its function.

Then, we take `USBDAQF1TD` for example.

### USBDAQF1TD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>

## Thermocouple interfacing SOP 

Create device handle -> Connect to device -> Open Thermal port -> Set Thermal parameters ->  Read thermocouple data -> Close Thermal port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `USBDAQF1TD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.