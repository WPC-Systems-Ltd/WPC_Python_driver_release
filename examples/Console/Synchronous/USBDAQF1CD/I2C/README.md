# I2C
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to read and write EEPROM (24C08C) through I2C interface.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### Hardware Requirements

To run this example, you will need a USBDAQF1CD product, which contains I2C master interface.

Then, we take `USBDAQF1CD` for example and use 24C08C as I2C slave, which connect directly to `USBDAQF1CD`.

For more information, please refer to datasheet of the [24C08C EEPROM](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### USBDAQF1CD (I2C Master)

|  Model name      | port | Serial clock (SCL) | Serial data (SDA)|
| -----------------|:----:|:------------------:|:----------------:|
| USBDAQF1CD       | I2C1 |        P2.6        |   P2.7           |

**Note:** External pull-up resistors (3.3 kΩ) are required for SDA/SCL pin.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1CD.JPG" alt="drawing" width="600"/>


### EEPROM 24C08C (I2C Slave)

|   EEPROM P/N     | pin8 (VCC) | pin7 (WP) | pin6 (SCL) | pin5 (SDA) | pin4 (GND) |
|:----------------:|:----------:|:---------:|:----------:|:----------:|:----------:|
| 24C08C           |    3.3V    |    GND    | P2.6       | P2.7       | GND        |

**Note:** The pin `WP` in 24C08C should tight to ground.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/25C08C.JPG" alt="drawing" width="400"/>

## I2C Interfacing SOP

1. Create device handle
2. Connect to device
3. Open I2C port
4. Set I2C parameters
5. Write data via I2C
6. Read data via I2C
7. Close I2C port
8. Disconnect device
9. Release device handle

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)