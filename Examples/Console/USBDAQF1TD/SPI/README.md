
# SPI
> **Note**
> Make sure you are connected to correct IP or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write EEPROM (25LC640) through SPI interface.

In order to use API correctly, please refer [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

If you want to build your own SPI application (for example, read the temperature data from external sensor with SPI interface), try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get USBDAQF1TD product, which contains SPI master interface.

Then, we take `USBDAQF1TD` for example and use 25LC640 as SPI slave, which connect directly to `USBDAQF1TD`.

For more information, please refer to datasheet of the [25LC640 EEPROM](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### USBDAQF1TD (SPI Master)

|   Model name     | port | MOSI | MISO | SCK  |  CS  |
| -----------------|:----:|:----:|:----:|:----:|:----:|
| USBDAQF1TD   | SPI1 | P2.3 | P2.2 | P2.1 | P2.0 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>


### EEPROM 25LC640 (SPI Slave)

| EEPROM P/N | pin8 (VCC) | pin7 (HOLD) | pin3 (WP) | pin5 (SI) | pin5 (SO) | pin6 (SCK) | pin1 (CS) | pin4 (Vss) |
|:----------:|:----------:|:-----------:|:---------:|:---------:|:---------:|:----------:|:---------:|:----------:|
|25LC640     |    3.3V    |     3.3V    |    3.3V   |   P2.2    |    P2.3   |    P2.1    |    P2.0   |    GND     |

**Note:** The pin `WP` and `HOLD` in 25LC640 should tight to 3.3V or 5V.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/25LC640.JPG" alt="drawing" width="400"/>

## SPI interfacing SOP 

Create device handle -> Connect to device -> Open DO pins -> Open SPI port -> Set SPI parameters -> Write data via SPI -> Read data via SPI -> Close DO pins -> Close SPI port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `USBDAQF1TD` successfully.

## SPI write
CS low -> write `WREN` bytes -> CS High -> CS low -> Write bytes into address -> CS High

## SPI read
CS low -> Read bytes from address -> CS High

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.