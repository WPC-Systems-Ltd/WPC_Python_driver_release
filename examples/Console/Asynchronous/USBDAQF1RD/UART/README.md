# UART (Asynchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle UART communications using asynchronous mode.
The example covers various UART operations including device configuration, data transfer, and event handling.

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

To run this example, you will need a USBDAQF1RD product with UART capability.

Here we use USBDAQF1RD as an example.

### USBDAQF1RD

|   Model name     | port  | RX   | TX   |
| -----------------|:-----:|:----:|:----:|
| USBDAQF1RD       | UART2 | P1.2 | P1.3 |

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-USBDAQF1RD.JPG" alt="drawing" width="600"/>

## UART Interfacing SOP

1. Create device handle
2. Connect to device
3. Open UART port
4. Set UART parameters
5. Write data via UART
6. Read data via UART
7. Close UART port
8. Disconnect device
9. Release device handle

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify UART connections
   - Solution: Check power supply

2. Communication Issues
   - Solution: Verify baud rate
   - Solution: Check data format
   - Solution: Monitor signal levels

3. Asynchronous Operation Issues
   - Solution: Check for proper event handling
   - Solution: Verify callback functions
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)