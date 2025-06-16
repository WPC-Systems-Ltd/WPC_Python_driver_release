# Counter (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle counter operations using asynchronous mode.
The example covers various counter operations including frequency measurement, pulse counting, and quadrature encoding.

Asynchronous mode is recommended when:
- You need concurrent operations
- You want non-blocking code execution
- You're working with multiple devices
- You need real-time data processing
- You want to handle multiple tasks simultaneously
- You need event-driven programming
- You want to maintain responsive UI during operations

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

To run this example, you will need a USBDAQF1AD product, which contains Counter function.

Here we use USBDAQF1AD as an example.

### USBDAQF1AD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1AD.JPG" alt="drawing" width="600"/>

## Counter Interfacing SOP

1. Create device handle
2. Connect to device
3. Open counter
4. Set counter parameters
5. Start counter
5. Read counter position
6. Stop counter
7. Close counter
8. Disconnect device
9. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify network connection

2. Counter Accuracy Issues
   - Solution: Check signal conditioning
   - Solution: Verify input signal levels
   - Solution: Check for noise interference

3. Asynchronous Operation Issues
   - Solution: Check for proper event handling
   - Solution: Verify callback functions
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)