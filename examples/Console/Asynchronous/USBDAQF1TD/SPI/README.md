# SPI
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write EEPROM (25LC640) through SPI interface.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1TD product, which contains SPI master interface.

Then, we take `USBDAQF1TD` for example and use 25LC640 as SPI slave, which connect directly to `USBDAQF1TD`.

For more information, please refer to datasheet of the [25LC640 EEPROM](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### USBDAQF1TD (SPI Master)

|   Model name     | port | MOSI | MISO | SCK  |  CS  |
| -----------------|:----:|:----:|:----:|:----:|:----:|
| USBDAQF1TD       | SPI1 | P2.3 | P2.2 | P2.1 | P2.0 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>


### EEPROM 25LC640 (SPI Slave)

| EEPROM P/N | pin8 (VCC) | pin7 (HOLD) | pin3 (WP) | pin5 (SI) | pin5 (SO) | pin6 (SCK) | pin1 (CS) | pin4 (Vss) |
|:----------:|:----------:|:-----------:|:---------:|:---------:|:---------:|:----------:|:---------:|:----------:|
|25LC640     |    3.3V    |     3.3V    |    3.3V   |   P2.2    |    P2.3   |    P2.1    |    P2.0   |    GND     |

**Note:** The pin `WP` and `HOLD` in 25LC640 should tight to 3.3V or 5V.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/25LC640.JPG" alt="drawing" width="400"/>

## SPI Interfacing SOP

Create device handle -> Connect to device -> Open DO pins -> Open SPI port -> Set SPI parameters -> Write data via SPI -> Read data via SPI -> Close DO pins -> Close SPI port -> Disconnect device -> Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1TD.

## SPI write
CS low -> write `WREN` bytes -> CS High -> CS low -> Write bytes into address -> CS High

## SPI read
CS low -> Read bytes from address -> CS High

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.