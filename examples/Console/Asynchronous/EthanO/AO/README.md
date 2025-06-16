# AO (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to output analog signals using asynchronous mode.
The example covers analog output operations in various modes.

Asynchronous mode is recommended when:
- You need to perform multiple operations concurrently
- You want to handle I/O operations without blocking the main thread
- You need to manage multiple devices simultaneously
- You want to implement event-driven programming patterns

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
- asyncio (for asynchronous operations)

## Hardware Requirements

To run this example, you will need a EthanO product, which contains AO function.

Here we use EthanO as an example.

### EthanO

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanO.JPG" alt="drawing" width="600"/>

## AO Interfacing SOP

## AI Interfacing SOP

1. Create device handle
2. Connect to device
3. Open AO port
4. Configure AO parameters
5. Open AO streaming
6. Start AO streaming
7. Close AO streaming
8. Close AO port
9. Disconnect device
10. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify network connection

2. Output Issues
   - Solution: Check voltage range settings
   - Solution: Verify channel configuration
   - Solution: Check output mode settings

3. Asynchronous Operation Issues
   - Solution: Ensure proper async/await syntax
   - Solution: Check event loop handling
   - Solution: Verify proper exception handling in async context

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)