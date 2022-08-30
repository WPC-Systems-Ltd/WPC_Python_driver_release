## Overview

The project `example_I2C_write_read.py` demonstrates how to use WPC python driver to read and write EEPROM (24C08C) through I2C interface.

If you want to build your own I2C application (for example, read the temperature data from external sensor with I2C interface), try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should get one of WPC-USB-DAQ series product as well as -AOD, -AD, -D, -TD, -CD and -RD, those contain I2C master interface.

Then, we take `WPC-USB-DAQ-F1-D` for example and use 24C08C as I2C slave, which connect directly to `WPC-USB-DAQ-F1-D`.

For more information, please refer to datasheet of the [24C08C EEPROM](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### WPC-USB-DAQ-F1-D (I2C Master)

|  Model name      | port | Serial clock (SCL) | Serial data (SDA)|
| -----------------|:----:|:------------------:|:----------------:|
| WPC-USB-DAQ-F1-D | I2C1 |        P2.6        |   P2.7           |

**Note:** External pull-up resistors (3.3 kΩ) are required for SDA/SCL pin.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-D.JPG" alt="drawing" width="600"/>


### EEPROM 24C08C (I2C Slave)

|   EEPROM P/N     | pin8 (VCC) | pin7 (WP) | pin6 (SCL) | pin5 (SDA) | pin4 (GND) |
|:----------------:|:----------:|:---------:|:----------:|:----------:|:----------:|
| 24C08C           |    3.3V    |    GND    | P2.6       | P2.7       | GND        |

**Note:** The pin `WP` in 24C08C should tight to ground.

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/25C08C.JPG" alt="drawing" width="400"/>

## I2C interfacing SOP 

Create device handle -> Connect to device -> Open I2C port -> Set I2C parameters -> Write data via I2C -> Read data via I2C -> Close I2C port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.