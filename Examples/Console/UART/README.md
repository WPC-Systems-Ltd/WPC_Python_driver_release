## Overview

The project `example_UART_read.py` & `example_UART_write.py` demonstrate how to use WPC python driver to read and write through UART interface.

To be verified, please take another WPC USB DAQ device or other device which support UART interface.
We connect two device via UART so that we can communicate data.  

If you want to build your own UART application (for example, read the temperature data from external sensor with UART interface), try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should have one of WPC-USB-DAQ series product as well as, -AOD, -AD, -D, -TD, -CD and -RD, those contain UART interface.

Then, we take `WPC-USB-DAQ-F1-D` for example.

### WPC-USB-DAQ-F1-D

|   Model name     | port  | RX   | TX   |
| -----------------|:-----:|:----:|:----:|
| WPC-USB-DAQ-F1-D | UART2 | P1.2 | P1.3 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-D.JPG" alt="drawing" width="600"/>

## UART interfacing SOP 

Create device handle -> Connect to device -> Open UART port -> Set UART parameters -> Write data via UART -> Read data via UART -> Close UART port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.