# Relay (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle relay operations using asynchronous mode.
The example covers various relay operations including channel control, state management, and event handling.

Asynchronous mode is recommended when:
- You need concurrent operations
- You want non-blocking code execution
- You need real-time relay monitoring
- You're working with multiple relay channels
- You need to handle multiple events simultaneously
- You want to maintain system responsiveness
- You need to implement complex event-driven logic

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

To run this example, you will need a EthanL product with relay capability.

Here we use EthanL as an example.

### EthanL

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-EthanL.JPG" alt="drawing" width="600"/>

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify relay connections
   - Solution: Check power supply

2. Control Issues
   - Solution: Verify channel configuration
   - Solution: Check relay states
   - Solution: Monitor control signals

3. Asynchronous Operation Issues
   - Solution: Check event handlers
   - Solution: Verify callback functions
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)