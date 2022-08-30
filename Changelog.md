WPC Python driver release changelog
===================================


v0.0.13 Date: 2022/08/30, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add GUI example code : Example_thermocouple, Example_RTD, Example_analog_input_on_demand, Example_I2C, Example_SPI
- Add WPC_DAQ_Devices_User_Manual_r17
- Add README.md in `I2C` & `SPI` & `UART` & `DIO` example console folder
- Add 25C08C.JPG & 25LC640.JPG in `Pinouts` folder
- Add `Datasheet` folder in `Reference` folder
- Add 24C08C.pdf & 25LC640.pdf in `Datasheet` folder

### Changed
- Change WPC Python Version from `pywpc-0.2.0` to `pywpc-0.2.1` 
- Renamed case-sensitive folder

### Removed
- Remove WPC_DAQ_Devices_User_Manual_r16

v0.0.12 Date: 2022/08/23, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add example code packet classification
- Add GUI example code : Example_analog_output, Example_UART

### Changed
- Change WPC Python Version from `pywpc-0.1.19` to `pywpc-0.2.0`  
- Change folder name `Example_AI_streaming` to `Example_analog_input`
- Change folder name `System` to `System_Network`

v0.0.11 Date: 2022/08/17, Developer: Chunglee_people
---------------------------------------------------
### Removed
- Remove unnecessary files

v0.0.10 Date: 2022/08/17, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add github edit link in Sphinx
- Add product description
- Add `Port funtion table` rst link in function description
- Add error code file `WPC_error_code.csv`
- Add `Error table` and `Port funtion table` in sphinx

### Changed
- Change `Port funtionality compatibility` to `Port funtion table` in Readme.md
- Change `Board` to `Model` in Readme.md
- Change WPC Python Version from `pywpc-0.1.18` to  `pywpc-0.1.19`  

v0.0.9 Date: 2022/08/12, Developer: Chunglee_people
---------------------------------------------------
### Fixed
- Fix Wiki link in README.md

v0.0.8 Date: 2022/08/11, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add product description and picture in Sphinx home page
- Check pinstate when open function modules
- Add WPC_DAQ_Devices_User_Manual_r16.pdf and WPC_Wifi_Configuration_r1.pdf  in `Reference/Manuals`

### Changed
- Change WPC Python Version from `pywpc-0.1.17` to  `pywpc-0.1.18`  

### Fixed
- Fix print information when DO_closePort in example_DO_blinky_port.py
- Fix `Run example code in console` web link in README.md

### Removed
- Remove WPC-Ethan-F4_manual_R3.pdf and wpc-usb-daq-xx_manual_r5.pdf  in `Reference/Manuals`

v0.0.7 Date: 2022/08/08, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add Thermo example code
  - `Thermo/example_RTD_read_channel_data.py`
  - `Thermo/example_RTD_read_channel_status.py`

### Changed
- Change WPC Python Version from `pywpc-0.1.16` to  `pywpc-0.1.17`  
- Change example code name from
  - `example_Thermo_read_channel_status` to `example_TC_read_channel_status` 
  - `example_Thermo_read_channel_data` to `example_TC_read_channel_data` 
- Change folder name from `Thermo` to `Temperature`

v0.0.6 Date: 2022/08/02, Developer: Chunglee_people
---------------------------------------------------
 
### Added
- Add AO example code
  - `AIO/example_AO_write_all_channels.py`
  - `AIO/example_AO_write_one_channels.py`
  - `AIO/example_AIO_one_channel_loopback.py`
  - `AIO/example_AIO_all_channels_loopback.py`
- Add SPI example code
  - `SPI/example_SPI_read_and_write.py`
  - `SPI/example_SPI_read.py`
- Add I2C example code
  - `I2C/example_I2C_write_read.py`

### Changed
- Change WPC Python Version from `pywpc-0.1.15` to  `pywpc-0.1.16` 

v0.0.5 Date: 2022/07/29, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add CAN example code
  - `CAN/example_CAN_read.py`
  - `CAN/example_CAN_write.py`

### Changed
- Change WPC Python Version from `pywpc-0.1.14` to  `pywpc-0.1.15`  

v0.0.4 Date: 2022/07/20, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add Thermo example code
  - `Thermo/example_Thermo_read_channel_data.py`
  - `Thermo/example_Thermo_read_channel_status.py`
- Add UART example code
  - `UART/example_UART_read.py`
  - `UART/example_UART_write.py`

### Changed
- Change WPC Python Version from `pywpc-0.1.13` to  `pywpc-0.1.14`  
- Change folder name `General` to `System` in console and gui folder
- Change `wireless device` to `WIFI` in document
 
v0.0.3 Date: 2022/07/07, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add DIO example code in console
- Add `Waiting cursor` when broadcasting
- Add `WPC_Led_blue.png` & `WPC_Led_red.png` & `WPC_Led_green.png` files
- Add `checkConnectionStatus` function to protect UI from error
- Add led png file path
- Add DIO example code
  - `DIO/example_DI_read_in_pins.py`
  - `DIO/example_DI_read_in_slot.py`
  - `DIO/example_DO_write_in_pins.py`
  - `DIO/example_DO_write_in_slot.py` 
  - `DIO/example_DO_toggle_in_pins.py` 
  - `DIO/example_DO_toggle_in_slot.py`
  - `General/example_get_pinmode.py`

### Changed
- Change WPC Python Version from `pywpc-0.1.12` to  `pywpc-0.1.13` (templete, Need to verify)

v0.0.2 Date: 2022/07/01, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add trademark file path.
- Add pyd path.
- Driver example.
- Folder hierarchy: Examples  ---- Console  ----  AIO
                            |              |
                            |              |
                            |               ----  General
                            |
                              ---- GUI      ----  AIO
                                           |
                                           |
                                            ----  General

### Changed
- Change WPC Python Version from `pywpc-0.1.10` to  `pywpc-0.1.12`

v0.0.1 Date: 2022/06/29, Developer: Chunglee_people
---------------------------------------------------

### Added
-  example GUI `UIexample_AIStreaming` & `UIexample_Broadcasts` & `UIexample_get_device_info`.
