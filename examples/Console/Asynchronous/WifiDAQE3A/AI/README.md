# AI (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to acquire multi-channel AI data simultaneously using asynchronous mode.
The example covers data acquisition in on-demand, N samples, and continuous modes.

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

To run this example, you will need a WifiDAQE3A product, which contains AI function.

Here we use WifiDAQE3A as an example.

### WifiDAQE3A

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3A.JPG" alt="drawing" width="600"/>

## Sampling Rate

### The max sampling rate is dependent on the number of enabled channels.

| Product/channel | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|:----------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| USB-DAQ-F1-AD   | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|
| USB-DAQ-F1-AOD  | 16k | 8k  | 5.3k| 4k  | 3.2k| 2.6k| 2.2k| 2.0k|

### The max sampling rate is dependent on the number of enabled chip-selects.

| Product/CS  | 1  | 2  |3   |
|:------------|:--:|:--:|:--:|
| STEM        |12k |6k  |4k  |

### The max sampling rate is fixed.

| Product         |Sampling rate|
|:----------------|:-----------:|
| Ethan-A         | 20k         |
| Ethan-A2        | 10k         |
| Wifi-DAQ-E3-A   | 10k         |
| Wifi-DAQ-F4-A   | 20k         |
| Wifi-DAQ-E3-AH  | 10k         |
| Wifi-DAQ-E3-AOD | 10k         |

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify network connection

2. Sampling Rate Issues
   - Solution: Reduce number of enabled channels
   - Solution: Check product specifications

3. Asynchronous Operation Issues
   - Solution: Ensure proper async/await syntax
   - Solution: Check event loop handling
   - Solution: Verify proper exception handling in async context

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)