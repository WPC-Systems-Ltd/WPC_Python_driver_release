## Overview

The project `example_TC_read_channel_data.py` & `example_TC_read_channel_status.py` demonstrate how to use WPC python driver to read thermocouple sensor temperature in Celcius.

If you want to build your own thermocouple application, try to use this as a basic template, then add your own code.

## How to use this example

### Hardware Requirement

In order to run this example, you should have `WPC-USB-DAQ-F1-TD` product with thermocouple sensor.

Then, we take `WPC-USB-DAQ-F1-TD` for example.

### WPC-USB-DAQ-F1-RD

<img src="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/Reference/Pinouts/USB-DAQ-F1-TD.JPG" alt="drawing" width="600"/>

## Thermocouple interfacing SOP 

Create device handle -> Connect to device -> Open Thermal port -> Set Thermal parameters ->  Read thermocouple data -> Close Thermal port -> Disconnect device -> Release device handle.

If function return value is 0, it represents communication with `WPC-USB-DAQ-F1-TD` successfully.

## Troubleshooting

For any technical support, please register new [issue](https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/issues) on GitHub.