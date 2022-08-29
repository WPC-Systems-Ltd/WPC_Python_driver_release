## Overview

The project `example_I2C_write_read.py` demonstrates how to use WPC python driver to read and write EEPROM (24C08C) through I2C interface.

If you want to build your own I2C application (for example, read the temperature data from external sensor with I2C interface), try to use this as a basic template, then add your own code.

## How to use example

### Hardware Required
In order to run this example, you should have one of WPC-USB-DAQ series product as well as a -AOD, -AD, -D, -TD, -CD and -RD, those contain I2C master interface.

Then, we take `WPC-USB-DAQ-F1-D` for example and use 24C08C as I2C slave, which connect with `WPC-USB-DAQ-F1-D`.

For more information about it, you can read the [datasheet of the 24C08C sensor](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### Pin Assignment:

**Note:** For full pin assignments of `WPC-USB-DAQ-F1-D`, please see [Pin Assignment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts).

**Note:** There's need to add an external pull-up resistors (3.3 kΩ) for SDA/SCL pin.

**Note:** The pin `WP` in 24C08C should tight to ground.

|                  | SDA             | SCL             |
|:----------------:|:---------------:|:---------------:|
| WPC-USB-DAQ-F1-D | I2C_MASTER_SDA1 | I2C_MASTER_SCL1 |
| 24C08C Sensor    | SDA             | SCL             |

Use `port2 pin 6` for I2C_MASTER_SDA1
Use `port2 pin 7` for I2C_MASTER_SCL1


## I2C interfacing SOP 

Create device handle -> Connect to device -> Open I2C port -> Set I2C parameters -> Write data via I2C -> Read data via I2C -> Close I2C port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## Troubleshooting

(For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.