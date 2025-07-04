# AIO (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle both analog input and output operations using asynchronous mode.
The example covers simultaneous AI/AO operations in various modes.

Asynchronous mode is recommended when:
- You need to perform multiple operations concurrently
- You want to handle I/O operations without blocking the main thread
- You need to manage multiple devices simultaneously
- You want to implement event-driven programming patterns
- You need real-time data processing with minimal latency
- You need to handle simultaneous input and output operations

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

To run this example, you will need a WifiDAQE3AOD product, which contains AIO function.

Here we use WifiDAQE3AOD as an example.

### WifiDAQE3AOD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3AOD.JPG" alt="drawing" width="600"/>

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify network connection

2. Data Accuracy Issues
   - Solution: Check signal conditioning
   - Solution: Verify grounding
   - Solution: Check for noise interference

3. Asynchronous Operation Issues
   - Solution: Ensure proper async/await syntax
   - Solution: Check event loop handling
   - Solution: Verify proper exception handling in async context

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)