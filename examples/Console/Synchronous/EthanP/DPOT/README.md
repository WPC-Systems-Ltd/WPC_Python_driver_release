# DPOT (Synchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle Digital Potentiometer (DPOT) operations using synchronous mode.
The example covers various operations including device configuration, resistance control, and event handling.

Synchronous mode is recommended when:
- You need simple, sequential operations
- You want straightforward, easy-to-understand code flow
- You don't need concurrent operations
- You're working with a single channel
- You prefer traditional procedural programming style
- You need predictable timing for resistance control
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

To run this example, you will need a EthanP product with DPOT capability.

Here we use EthanP as an example.

### EthanP

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanP.JPG" alt="drawing" width="600"/>

## DPOT Interfacing SOP

1. Create device handle
2. Connect to device
3. Open DPOT
4. Read/Write digital potentiometer resistance
5. Close DPOT
6. Disconnect device
7. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify device connections
   - Solution: Check power supply

2. Control Issues
   - Solution: Verify DPOT configuration
   - Solution: Check resistance settings
   - Solution: Monitor resistance changes

3. Synchronous Operation Issues
   - Solution: Check for blocking operations
   - Solution: Verify proper error handling
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)