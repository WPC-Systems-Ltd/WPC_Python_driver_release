## Overview
example_I2C_write_read demonstrates basic usage of WPC python driver by reading and writing from a I2C connected sensor:

If you have a new I2C application to go (for example, read the temperature data from external sensor with I2C interface), try this as a basic template, then add your own code.

## How to use example


### Hardware Required
To run this example, you should have one WPC-USB-DAQ series product as well as a AOD, AD, D, TD, CD and RD, which contains I2C protocol for master.

Then, we take `WPC-USB-DAQ-F1-D` for example and take 24C08C for I2C slave, which connect with WPC-USB-DAQ-F1-D.

For more information about it, you can read the [datasheet of the 24C08C sensor](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/Reference/Datasheet).

### Pin Assignment:
**Note:** For full pin assignments of WPC-USB-DAQ-F1-D, please see [Pin Assignment](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts).

**Note:** There's need to add an external pull-up resistors (3.3 kΩ) for SDA/SCL pin.

**Note:** The pin of `WP` in 24C08C should connect to ground.

|                  | SDA             | SCL             |
| ---------------- | ----------------| ----------------|
| WPC-USB-DAQ-F1-D | I2C_MASTER_SDA1 | I2C_MASTER_SCL1 |
| 24C08C Sensor    | SDA             | SCL             |

Use `port2 pin 6` for I2C_MASTER_SDA1
Use `port2 pin 7` for I2C_MASTER_SCL1 


## Example code step 

Create handle -> Connect -> Open I2C port -> Set I2C parameter -> Write data via I2C -> Read data via I2C -> Close I2C port -> Disconnect -> Release handle

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-D` successfully.

## Troubleshooting

(For any technical queries, please open an [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub. We will get back to you as soon as possible.)