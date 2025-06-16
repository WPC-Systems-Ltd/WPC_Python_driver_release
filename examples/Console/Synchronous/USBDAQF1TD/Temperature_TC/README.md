# Temperature TC (Synchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle Thermocouple (TC) temperature measurements using synchronous mode.
The example covers various TC operations including sensor configuration, data acquisition, and event handling.

Synchronous mode is recommended when:
- You need simple, sequential operations
- You want straightforward, easy-to-understand code flow
- You don't need concurrent operations
- You're working with a single sensor
- You prefer traditional procedural programming style
- You need predictable timing for temperature measurements
- You need precise control over operation sequence

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

## Installation

```bash
pip install wpcsys
```

## Dependencies

- Python 3.8 or higher (up to 3.12)
- wpcsys package
- numpy (for data processing)
- matplotlib (for data visualization, optional)

## Hardware Requirements

To run this example, you will need a USBDAQF1TD product with Thermocouple capability.

Here we use USBDAQF1TD as an example.

### USBDAQF1TD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1TD.JPG" alt="drawing" width="600"/>

## Thermocouple Interfacing SOP

1. Create device handle
2. Connect to device
3. Open thermal port
4. Set thermal parameters
5. Read thermocouple data
6. Close thermal port
7. Disconnect device
8. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify sensor connections
   - Solution: Check power supply

2. Temperature Issues
   - Solution: Verify sensor type configuration
   - Solution: Check cold junction compensation
   - Solution: Monitor sensor readings

3. Synchronous Operation Issues
   - Solution: Check for blocking operations
   - Solution: Verify proper error handling
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)