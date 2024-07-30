# RTC-AI
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This example project demonstrates how to use RTC-AI with WPC python driver.

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

To create your own application, start with this simple template and then include your custom code.

### Hardware Requirements

To run this example, you will need a EthanA2 product, which contains RTC-AI function

Then, we take `EthanA2` for example.

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

A return value of 0 indicates successful communication with the EthanA2.

## Troubleshooting

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.