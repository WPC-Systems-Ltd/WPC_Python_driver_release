# AO
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use WPC python driver to output digital signal.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

## How To Use This Example

### AO output range

| Product         |AO range    |
|:---------------:|:----------:|
| USB-DAQ-F1-AOD  | 0 ~ 5 V    |
| Ethan-O         | -10 ~ 10 V |
| STEM            | -10 ~ 10 V |

### Hardware Requirements

To run this example, you will need a WifiDAQE3AOD product, which contains AO function.

Then, we take `WifiDAQE3AOD` for example.

### WifiDAQE3AOD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-WifiDAQE3AOD.JPG" alt="drawing" width="600"/>

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

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)