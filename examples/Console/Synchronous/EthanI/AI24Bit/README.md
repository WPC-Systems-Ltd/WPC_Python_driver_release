# AI24Bit (Synchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to acquire 24-bit high-resolution analog input data using synchronous mode.
The example covers data acquisition in various modes with high precision measurements.

Synchronous mode is recommended when:
- You need simple, sequential operations
- You want straightforward, easy-to-understand code flow
- You don't need concurrent operations
- You're working with a single device
- You prefer traditional procedural programming style
- You need predictable timing for data acquisition

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

To run this example, you will need a EthanI product, which contains 24-bit AI function.

Here we use EthanI as an example.

### EthanI

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanI.JPG" alt="drawing" width="600"/>

## Get AI Data

| Product |port | Description      |
|---------|-----|------------------|
| EthanA2 | 0   | Get voltage (V)  |

## AI Interfacing SOP

1. Create device handle
2. Connect to device
3. Open AI port
4. Read AI data on demand
5. Close AI port
6. Disconnect device
7. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify network connection

2. Data Accuracy Issues
   - Solution: Check signal conditioning
   - Solution: Verify grounding
   - Solution: Check for noise interference

3. Synchronous Operation Issues
   - Solution: Check for blocking operations
   - Solution: Verify proper error handling
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)