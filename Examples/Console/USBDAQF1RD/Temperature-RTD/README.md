
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read RTD sensor temperature in Celcius.

If you want to build your own RTD application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get `USBDAQF1RD` product, which contains RTD sensor and its function.

It support PT100 and PT1000 resistance thermometers, also called resistance temperature detectors (RTDs)

Then, we take `USBDAQF1RD` for example.

### USBDAQF1RD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USBDAQF1RD.JPG" alt="drawing" width="600"/>

## RTD interfacing SOP 

Create device handle -> Connect to device -> Open Thermal port -> Set Thermal parameters -> Read RTD data -> Close Thermal port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `USBDAQF1RD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.