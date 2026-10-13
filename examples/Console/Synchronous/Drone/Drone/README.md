# Drone (Synchronous Mode)
> **Note**
> Ensure you are connected to the correct IP address or serial number.

## Overview

This project demonstrates how to use the WPC Python driver to handle drone control operations using synchronous mode.
The example covers various operations including device configuration, flight control, and event handling.

Synchronous mode is recommended when:
- You need simple, sequential operations
- You want straightforward, easy-to-understand code flow
- You don't need concurrent operations
- You're working with a single drone
- You prefer traditional procedural programming style
- You need predictable timing for flight control
- You need precise control over operation sequence

For detailed API usage, refer to the [documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/).

## Installation

```bash
pip install wpcsys
```

## Dependencies

- Python 3.9 or higher (up to 3.12)
- wpcsys package
- numpy (for data processing)

## Hardware Requirements

To run this example, you will need a Drone product with drone control capability.

Here we use Drone as an example.

### Drone

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-Drone.JPG" alt="drawing" width="600"/>

### Nvidia Jetson Nano via USB to TTL

#### 1. Hardware Connection
Use a USB-to-TTL serial adapter to connect the Jetson Nano to the Drone.
Please cross-connect the RX and TX pins:
- USB-TTL **TX**  ➜  Drone **RX**
- USB-TTL **RX**  ➜  Drone **TX**
- USB-TTL **GND** ➜  Drone **GND**
*(Warning: Do not connect the VCC/5V/3.3V pin unless you intend to power the board via USB.)*

#### 2. Find the Serial Port
Plug the USB-to-TTL adapter into the Jetson Nano, then open a terminal and check the system logs to find the assigned port name:
```bash
dmesg | grep tty
```
You should see a message indicating the adapter was attached to a port like `ttyUSB0` or `ttyUSB1`.

Verify the device exists:
```bash
ls -l /dev/ttyUSB*
```

#### 3. Set Port Permissions
By default, standard users do not have permission to read/write serial ports on Linux.
You can grant temporary read/write access to the port (replace `ttyUSB0` with your actual port):
```bash
sudo chmod 666 /dev/ttyUSB0
```
*(For a permanent solution, add your user to the dialout group: `sudo usermod -a -G dialout $USER`, then reboot).*

#### 4. Run the Code
Update the port string in your Python script to match the port you found (e.g., `"/dev/ttyUSB0"`), and then execute the script.


For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)