## Overview

The project `example_SPI_write.py` & `example_SPI_read_and_write` demonstrate how to use WPC python driver to read and write EEPROM (25LC640) through SPI interface.

If you want to build your own SPI application (for example, read the temperature data from external sensor with SPI interface), try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should have one of WPC-USB-DAQ series product as well as, -AD, -D, -TD, -CD and -RD, those contain SPI master interface.

Then, we take `WPC-USB-DAQ-F1-D` for example and use 25LC640 as SPI slave, which connect directly to `WPC-USB-DAQ-F1-D`.

For more information, please refer to datasheet of the [25LC640 EEPROM](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### Pin Assignment

**Note:** For full pin assignments of `WPC-USB-DAQ-F1-D`, please see [Pin Assignment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Pinouts).

## WPC-USB-DAQ-F1-D

|                  | port | MOSI | MISO | SCK  |  CS  |
| -----------------|:----:|:----:|:----:|:----:|:----:|
| WPC-USB-DAQ-F1-D | SPI1 | P2.3 | P2.2 | P2.1 | P2.0 |

## 25LC640

|                  | VCC  | HOLD |  WP  |  SI  |  SO  | SCK  |  CS  | Vss  |
|:----------------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|      25LC640     | 3.3V | 3.3V | 3.3V | P2.2 | P2.3 | P2.1 | P2.0 | GND  |
**Note:** The pin `WP` and `HOLD` in 25LC640 should tight to 3.3V or 5V.


## SPI interfacing SOP 

Create device handle -> Connect to device -> Open DO pins -> Open SPI port -> Set SPI parameters -> Write data via SPI -> Read data via SPI -> Close DO pins -> Close SPI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## SPI write
CS low -> write `WREN` bytes -> CS High -> CS low -> Write bytes into address -> CS High

## SPI read
CS low -> Read bytes from address -> CS High

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.