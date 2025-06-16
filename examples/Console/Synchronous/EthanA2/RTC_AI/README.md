# RTC AI (Synchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle Real-Time Clock (RTC) and Analog Input (AI) operations using synchronous mode.
The example covers various operations including time synchronization, data acquisition, and event handling.

Synchronous mode is recommended when:
- You need simple, sequential operations
- You want straightforward, easy-to-understand code flow
- You don't need concurrent operations
- You're working with a single channel
- You prefer traditional procedural programming style
- You need predictable timing for data acquisition
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

To run this example, you will need a EthanA2 product with RTC and AI capability.

Here we use EthanA2 as an example.

### EthanA2

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanA2.JPG" alt="drawing" width="600"/>

## RTC-AI Interfacing SOP

1. Create device handle
2. Connect to device
3. Open AI port
4. Set AI parameters
5. Set AI trigger mode
6. Set RTC
7. Open AI streaming
8. Start RTC alarm
9. Read AI streaming
10. Close AI streaming
11. Close AI port
12. Disconnect device
13. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify device connections
   - Solution: Check power supply

2. Operation Issues
   - Solution: Verify time configuration
   - Solution: Check channel settings
   - Solution: Monitor data acquisition

3. Synchronous Operation Issues
   - Solution: Check for blocking operations
   - Solution: Verify proper error handling
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)