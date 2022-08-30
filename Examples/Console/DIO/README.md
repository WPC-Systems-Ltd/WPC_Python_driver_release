## Overview

DIO series example code demonstrate how to use WPC python driver to control DIO with whole port or assign pins 

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own DIO application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should have one of WPC-USB-DAQ series product as well as -DSNK, -AOD, -AD, -D, -TD, -CD and -RD or Ethan-D, those contain DIO components.

Then, we take `WPC-USB-DAQ-F1-D` for example.

### WPC-USB-DAQ-F1-D

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-D.JPG" alt="drawing" width="600"/>

## DIO interfacing SOP 

# DO
Create device handle -> Connect to device -> Open DO port / pins -> Write high or low to digital output -> Close DO port / pins -> Disconnect device -> Release device handle.

# DI
Create device handle -> Connect to device -> Open DI port / pins -> Read high or low from digital input -> Close DI port / pins -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.