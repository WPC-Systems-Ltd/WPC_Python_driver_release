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

1. Create device handle
2. Connect to device
3. Open DO pins
4. Open SPI port
5. Set SPI parameters
6. Write data via SPI
7. Read data via SPI
8. Close DO pins
9. Close SPI port
10 Disconnect device
11. Release device handle.

A return value of 0 indicates successful communication with the USBDAQF1TD.

## SPI Write
1. CS low
2. Write `WREN` bytes
3. CS high
4. CS low
5. Write bytes into address
6. CS high

## SPI Read
1. CS low
2. Read bytes from address
3. CS high

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.