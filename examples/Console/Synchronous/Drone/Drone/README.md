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

- Python 3.8 or higher (up to 3.12)
- wpcsys package
- numpy (for data processing)
- matplotlib (for data visualization, optional)

## Hardware Requirements

To run this example, you will need a Drone product with drone control capability.

Here we use Drone as an example.

### Drone

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/pinout-Drone.JPG" alt="drawing" width="600"/>

## Operating Procedure

### Pre-Flight Checklist

- Ensure the drone's **center of gravity** is properly balanced.
- Verify that all **mounted payloads are securely fastened**.
- Confirm that **all screws on the drone are tightened**.
- Check that the **drone battery is fully charged** (approximately **12.5V**).
- Make sure the **USB drive has sufficient storage** to record the flight data.
- Insert the **USB drive into the flight control computer**.

> 💡 **If the USB drive is not inserted, the drone system will not function.**

### Connect the Battery Power

- After connecting the drone battery, the motors will emit a **short "beep" every second**.

### Unlock the Drone

- On the **emergency power switch**, press **"On"** to supply power.
- Then turn on the **flight control computer**.

> 💡 **If the flight control system is not powered on, the drone system will not function.**

### Wait for Flight Control Initialization

- Wait approximately **2 minutes** for the flight control system to start.
- You will hear a **long "beep"** from the motors indicating it's ready.

### Operate the Drone via Remote or Mission Computer

- For detailed control instructions, please refer to the [**user guide**](https://wpc.super.site/3kg-class-uav-platform-user-guide) or [**video**](https://www.youtube.com/watch?v=MCejJsEQymk).

### End of Operation & Landing

- If the battery level is low, **disconnect the drone battery and replace it** as needed.

## Troubleshooting

Common issues and their solutions:

1. Connection Error
   - Solution: Check IP address or serial number
   - Solution: Verify device connections
   - Solution: Check power supply

2. Control Issues
   - Solution: Verify drone configuration
   - Solution: Check sensor settings
   - Solution: Monitor flight status

3. Synchronous Operation Issues
   - Solution: Check for blocking operations
   - Solution: Verify proper error handling
   - Solution: Ensure proper resource cleanup

For technical support, please register a new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.

## Reference

1. [WPC official website](https://www.wpc.com.tw/)
2. [WPC technical support center](https://wpc.super.site/)
3. [WPC Python driver documentation](https://wpc-systems-ltd.github.io/WPC_Python_driver_release/)