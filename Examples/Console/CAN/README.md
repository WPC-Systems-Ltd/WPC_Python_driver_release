## Overview

This example project demonstrates how to use WPC python driver to read and write through CAN interface.

In order to verify, please take another `WPC-USB-DAQ-F1-CD` or other device which support CAN interface.
We connect two device via CAN so that can communicate data.  

If you want to build your own CAN application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to verify, please get two  WPC-USB-DAQ-F1-CD devices or one with any other device which support CAN interface.

Then, we take `WPC-USB-DAQ-F1-CD` for example.

### WPC-USB-DAQ-F1-CD

Both connect CAN_H to CAN_H and CAN_L to CAN_L then short pin35, pin36 together for enabling termination resistor.
 

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-CD.JPG" alt="drawing" width="600"/>


## CAN interfacing SOP 

Create device handle -> Connect to device -> Open CAN port -> Set CAN parameters -> Write data via CAN -> Read data via CAN -> Close CAN port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-CD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.