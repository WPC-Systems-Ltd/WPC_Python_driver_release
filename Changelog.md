WPC Python driver release changelog
===================================


v3.1.7 Date: 2025/06/16, Developer: Chunglee_people
---------------------------------------------------
### Added 
- Add `Supported Platforms` in README 
- Add -8012, -9400, -9401, -9402 error code 
- API: Drone_getFirmwareVersion, Drone_getSerialNumber
 
### Changed
- All the example code will follow PEP8 rule
- Drone's UART read time
 
v3.1.2 Date: 2024/08/01, Developer: Chunglee_people
---------------------------------------------------
### Added
- Support Python 3.11, 3.12
- Verify example code with python 3.11 & 3.12
- error code: 8107 - The DI channel is not available
- error code: 8108 - The DO channel is not available
- error code: 8205 - The AI trigger mode is not valid or is not recognized
- DIO example code in Wifi-DAQ-E3-AOD
- RTC example code: RTC_trigger_AI_N_samples, RTC_trigger_AI_continuous
- Broadcast example code: find_networkdevices_blink
- system example code: get_device_alias, set_device_alias
- SNTP example code: SNTP configure
- AI API: AI_openStreaming, AI_startStreaming, AI_closeStreaming, AI_setTriggerMode, get_device_alias, set_device_alias, Bcst_checkMACAndRing
- Ethan series devices support `SNTP` module
- EthanA & EthanA2 support `RTC_AI` module

### Changed
- Rename AI API name: AI_stop -> AI_closeStreaming, AI_start -> AI_startStreaming

### Fixed
- Synchronize product feature with WPC official DM

v3.0.27 Date: 2024/05/20, Developer: Chunglee_people
---------------------------------------------------
### Added
- Fix the bug of couner and encoder

v3.0.26 Date: 2024/05/13, Developer: Chunglee_people
---------------------------------------------------
### Added
- New product: EthanA2
- Add encoder, SD function
- error code: 8106,The counter channel is not available
- example code: Encoder_read, SD_read, SD_write, RTC_trigger_AI_continuous, RTC_trigger_AI_N_samples, RTC_trigger_AI_on_demand, DPOT_writeByChannel
- API: DPOT_writeByChannel, AI_getData, Sys_startRTCAlarm, Sys_stopRTCAlarm

v3.0.23 Date: 2024/03/29, Developer: Chunglee_people
----------------------------------------------------
### Fixed
- Unify example code's printf style

v3.0.22 Date: 2024/03/28, Developer: Chunglee_people
----------------------------------------------------
### Added
- Verify EDriveST example code
- Add the argument of `port` in relay relatie API
- Example code: get_serial_number.py, AHRS_getAcceleration.py, AHRS_getAngularVelocity.py
AHRS_getEstimation.py, AHRS_getOrientation.py
- Error code: -8105 (relay port)
- image: product-EthanIA.jpg
- API: AHRS_getAcceleration, AHRS_getAngularVelocity

### Fixed
- Sync API description with C#
- Product summary
- Bug of using wrong `Sys_getDriverInfo` API in async example code
- Modify the API description of Motion_cfgLimit `en_forward` and `en_reverse`
- Modify the API description of Motion_getProcessState
- README.md: AHRS, AI24bit, DPOT, Motion, Drive
- Error code: The error code `-9301` description
- Example code: DI pin index in DIO_loopback_pins

### Removed
- Example code: get_USB_info, AHRS_read
- API: AHRS_setSamplingPeriod, Motion_getParameters, Motion_loadParameters, Motion_saveParameters

v3.0.19 Date: 2024/03/01, Developer: Chunglee_people
----------------------------------------------------
### Added
- New product: EthanP, EthanEX_D, EthanIA
- Folder: Material
- -9300/ -9301/ -8401 error code
- API: AHRS_getEstimate

### Fixed
- Class: WifiDAQE3AH

### Removed
- API: AHRS_readStreaming

v3.0.18 Date: 2024/02/26, Developer: Duflosth
---------------------------------------------
### Added
- The file AHRS_visualize_Qt.py that provides an interactive sensor visualisation interface
- viz_data folder, with plane images, 7 digit police, and themeWPC.qss for the style the PyQt interface

### Changed
- The file AHRS_visualize.py: added animated pitch/roll/yaw plane images

### Removed
- Unnecessary code in AHRS_visualize.py
- Data folder in AHRS/

v3.0.17 Date: 2024/02/05, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add `numpy-stl>=3.1.1` in requirements.txt
- Integrated motion command and its API
- API: AHRS_setSamplingPeriod

### Fixed
- example code: AHRS_visualize.py

v3.0.14 Date: 2023/12/18, Developer: Chunglee_people
----------------------------------------------------
### Added
- API: AHRS_setSamplingPeriod
- example code: AHRS_visualize.py and its data folder

### Fixed
- example code: AHRS_read.py

### Removed
- Remove "mask" parameter in AHRS_start
- API: AHRS_setGeneral
- ``timeout=timeout`` in example code

v3.0.13 Date: 2023/12/13, Developer: Chunglee_people
----------------------------------------------------
### Added
- Sampling rate chart in AI README.md
- function description: AI_enableCS
- AI Max Sampling Rate Table

### Fixed
- Synchronize error code with CSharp

### Removed
- examples_GUI_Asynchronous.rst
- example code: AI_N_samples_in_loop

v3.0.12 Date: 2023/12/08, Developer: Chunglee_people
----------------------------------------------------
### Added
- STEM's pinout
- example code: set_LED_status
- API: Wifi_getPowerGoodStatus, Wifi_getChargeStatus
Wifi_resetLED, Wifi_setBlueLED, Wifi_setRedLED, Wifi_setGreenLED

### Fixed
- Synchronous GUI example code: AI

### Removed
- GUI example code: Asynchronous

v3.0.11 Date: 2023/12/04, Developer: Chunglee_people
----------------------------------------------------
### Added
- example code: AI_continuous_multi_slot, AO_output_while_AI_streaming.
- API: _AI_getCounter, Sys_getPythonVersion
- Doc: Description in AI_enableCS
- Error class: APINotSupportError
- Channel count vs. sampling rate in AI README.md
- The limitation of the sampling rate in AIO README.md
- AO output range in AO README.md

### Fixed
- Each slot has it own chip_select variable
- Buf of calculating wrong index in `_AI_changePortToIndex`

v3.0.8 Date: 2023/11/23, Developer: Chunglee_people
---------------------------------------------------
### Fixed
- Fix AI readStreaming's returned data length

v3.0.7 Date: 2023/11/20, Developer: Chunglee_people
---------------------------------------------------
### Fixed
- Fix module reopen issue

v3.0.6 Date: 2023/11/16, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add example code: AHRS_read.cs

v3.0.5 Date: 2023/10/16, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add reboot example code in hello world.py
- Ubuntu's os badge

v3.0.3 Date: 2023/09/25, Developer: Chunglee_people
---------------------------------------------------
### Fixed
- AO function generation code

v3.0.2 Date: 2023/09/23, Developer: Chunglee_people
---------------------------------------------------
### Added
- New modules: Counter and PWM

### Changed
- USB DAQ series's pinout with PWM & channel supported

### Fixed
- example code(async): I2C_write_read and SPI_read_and_write content

v3.0.1 Date: 2023/09/06, Developer: Chunglee_people
---------------------------------------------------
### Added
- API: _Wifi_resetAIBuffer

### Changed
- API name: _setWifiBandwidth->Wifi_setBandwidth

### Fixed
- Sphinx main page

v3.0.0 Date: 2023/07/28, Developer: Chunglee_people
---------------------------------------------------
### Added
- Support Linux Ubuntu22.04

### Fixed
- Keyword, author name, install_requires in setup.py

### Removed
- PyQt5Designer in requirements.txt

v2.1.7 Date: 2023/07/27, Developer: Chunglee_people
---------------------------------------------------
### Added
- version.py in wpcsys package

### Fixed
- API name: _Drive_ssetEncoderPosition-> _Drive_setEncoderPosition
- Use version.py's version instead of pywpc's

### Removed
- latest version in README.rst

v2.1.6 Date: 2023/07/18, Developer: Chunglee_people
---------------------------------------------------
### Added
- New product: `EthanI` & `EthanT`

v2.1.5 Date: 2023/07/14, Developer: Chunglee_people
---------------------------------------------------
### Added
- New product: `EDrive-ST`

v2.1.4 Date: 2023/06/08, Developer: Chunglee_people
---------------------------------------------------
### Added
- New product: `WifiDAQF4A`
- Add STEM port supplementary note

### Fixed
- `STEM` has not supported `AO_waveform_gen` yet
- Bug of missing `AI_stop` in AI series example code
- If the product is `STEM`, use slot instead of port

v2.1.2 Date: 2023/06/05, Developer: Chunglee_people
---------------------------------------------------
### Added
- STEM product introduction

### Changed
- STEM product images
- API name:
  - Wifi_readAccleration -> Wifi_readAcceleration

### Fixed
- AIO & DIO example code's description
- Firmware error code

### Removed
- Remove pywpc.__version__ in README.rst

v2.1.1 Date: 2023/06/03, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add STEM product

### Changed
- Select cs pin based on the SPI port.

v2.0.3 Date: 2023/03/25, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add default value in example code and API

### Removed
- DIO series example code in EthanL
- DataLogger in HANDLE_LIST
- Return type of Motion_checkRef

v2.0.2 Date: 2023/03/22, Developer: Chunglee_people
---------------------------------------------------
### Added
- Example codes:
  - Relay_read_counters, Relay_set_channel, Motion_servo_on, Motion_position_blending
- Error class:
  - RelayCounterIndexError
- Release new API(sync and async):
  - Motion_enableServoOff, Motion_enableServoOn, Motion_overrideAxisPosi, Motion_getLogicalPosi, Motion_getEncoderPosi
- Add Datalogger in each product

### Changed
- WifiDAQE3A product image
- API & argument name
  - Motion_opencfgFile -> Motion_openCfgFile
  - Motion_opencfgFile_async -> Motion_openCfgFile_async
  - target_position -> target_posi
  - veloctity -> velo

### Fixed
- Bug of missing connect and disconnect in find all device example code
- Delay 500ms before reading `Thermal_readSensor` in example code

### Removed
- API:
  - Motion_enableServoOn_async & Motion_enableServoOn

v2.0.1 Date: 2023/03/09, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add `serial_num ='default'` in USB series product
- Add `ip= '192.168.5.79'` in Wifi series product
- Add `ip= '192.168.1.110'` in Ethan series product

### Changed
- Sync C# & python in example code

v2.0.0 Date: 2023/02/03, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add synchronous console and GUI example code
- Add asynchronous and synchronous mode description in readme.rst

v1.1.3 Date: 2023/01/18, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add three scenario when run asyncio function
  - asyncio.run(main()) ## Use terminal
  - await main() ## Use Jupyter or IPython(>=7.0)，
  - main_for_spyder ## Use Spyder

v1.1.2 Date: 2023/01/07, Developer: Chunglee_people
---------------------------------------------------
### Added
- Product:
  - Emotion
- Example codes :
  - Motion_find_home.py, Motion_find_limit.py and Motion_find_index.py,
  - Motion_velocity_blending.py and Motion_velocity_blending_accerleration,
  - Motion_load_configuration_file.py and Motion_set_configuration_file,
  - Motion_1axis_move_with_alarm_in.py, Motion_1axis_move_with_inposition.py, Motion_1axis_move_with_breakpoint.py,
	  Motion_1axis_move_with_configuration_file.py, Motion_1axis_move_with_capture.py and Motion_1axis_move_with_S_curve_acceleration.py
  - Motion_2axis_circular_interpolation.py and Motion_2axis_linear_interpolation.py
  - Motion_3axis_linear_interpolation.py and Motion_3axis_helical_interpolation.py
  - Motion_3axis_synchronous_move.cs and Motion_3axis_asynchronous_move.cs
- Reference :
  - WPC_MCX_H_Motion_Manual_r25

### Changed
- Update `WPC_DAQ_Devices_User_Manual` from r20 to r23

v1.1.0 Date: 2022/11/23, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add handle combobox in GUI example code
- Add product `EthanL` & `EthanO`
- Add `AO_waveform_generation.py` example code

### Changed
- Update `WPC_DAQ_Devices_User_Manual` from r19 to r20


v1.0.9 Date: 2022/11/04, Developer: Chunglee_people
---------------------------------------------------
### Fixed
- Fix example code website

v1.0.8.1 Date: 2022/11/04, Developer: Chunglee_people
------------------------------------------------------
### Removed
- Remove old `Examples` folder

v1.0.8 Date: 2022/11/04, Developer: Chunglee_people
---------------------------------------------------
### Added
- Each product has its own example codes
- Add README.md in console - AI folder
- Add firmware error code
- Add `libusb-1.0.dll`
- Included dll in `MANIFEST.in`

### Changed
- Replace `README.md` with `README.rst`

### Fixed
- Fix AI & CAN API error

v1.0.3 Date: 2022/10/20, Developer: Chunglee_people
---------------------------------------------------
### Added
- Add `AI_setMode_async` in AI_ondemand example code
- Add logger example code `example_AI_continuous_with_logger` & `example_RTD_read_channel_data_with_logger` & `example_TC_read_channel_data with_logger`

### Fixed
- Fix sphinx homepage content
- Fix GUI `Example_analog_input` code

v1.0.2.1 Date: 2022/10/14, Developer: Chunglee_people
------------------------------------------------------
### Added
- Add .nojekyll
- Add `WPC_7steps_Of_Python_Project_Workflow_r6.pdf` in Reference/Manuals

v1.0.2 Date: 2022/10/13, Developer: Linc
----------------------------------------
### Added
- `distclass` option in `setup`

### Changed
- Made install requirement read from `requirements.txt`

### Removed
- Version-dependent Python requirement

### Fixed
- Bug of version
- Bug of classifier string


v1.0.1 Date: 2022/10/12, Developer: Chunglee_people
----------------------------------------------------
### Added
- Update wpcsys in PyPI depended on conda environment version
- Add get release version and get python version in setup.py
- Add classifiers in setup.py
- Add `Useful conda commands` in wiki page
- Add `from wpcsys import pywpc` in version.py

### Changed
- Change WPC Python Version from `pywpc-1.0.0` to `pywpc-1.0.1`
- Change device handle name `Broadcaster` to `DeviceFinder`
- Change description name from `WPC Device Driver Python API` to `WPC Systems Python API` in setup.py

### Fixed
- Fix python_requires depends on conda environment version
- Fix version return value at System_Network in Example_find_all_device

### Removed
- Remove `pywpc.__version__` at Quick Start in README.md
- Remove driver release date in sphinx
- Remove unsupported products from README.md

v1.0.0 Date: 2022/10/04, Developer: Chunglee_people
----------------------------------------------------
### Added
- From this version, we will release pywpc.pyd for python3.8, python3.9 and python3.10 in PyPI
- Add `PyQt5Designer` in requirements.txt and setup.py

### Changed
- Change API name to XXX_async
- Change WPC Python Version from `pywpc-0.2.7` to `pywpc-1.0.0`
- Update `wpcsys` in 1.0.0

v0.0.20 Date: 2022/10/04, Developer: Chunglee_people
----------------------------------------------------

### Changed
- Change WPC Python Version from `pywpc-0.2.6` to `pywpc-0.2.7`
- Update `wpcsys` in 0.2.7

### Fixed
- Fix bug of AI module in EthanA

v0.0.19 Date: 2022/10/03, Developer: Chunglee_people
----------------------------------------------------
### Changed
- Change WPC_DAQ_Devices_User_Manual to R18
- Change WPC Python Version from `pywpc-0.2.5` to `pywpc-0.2.6`
- Update `wpcsys` in 0.2.6

### Fixed
- Fix bug of DI module in EthanD

v0.0.18 Date: 2022/09/30, Developer: Chunglee_people
----------------------------------------------------
### Changed
- Update `wpcsys` in 0.2.5
- Change WPC Python Version from `pywpc-0.2.4` to `pywpc-0.2.5`

### Fixed
- Fix bug of missing EthDevice initial

v0.0.17 Date: 2022/09/27, Developer: Chunglee_people
----------------------------------------------------
### Added
- Update `wpcsys` in 0.2.4

### Fixed
- Fix bug in WifiSystemModule
- Fix duplicated decription in README.md

v0.0.16 Date: 2022/09/26, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add mode 1 (Reserved) in `UART_setParity`

### Changed
- Change WPC Python Version from `pywpc-0.2.3` to `pywpc-0.2.4`
- Change sphinx project name from `WPC Device Driver` to `WPC Python driver`
- Change sphinx index.rst title from `WPC DAQ Device Programming Guide` to `WPC Python Driver Programming Guide`
- Uniform name to `WPC Python driver` in project
- Change sphinx project name from `WPC Device Driver` to `WPC Python device driver`
- Change sphinx index.rst title from `WPC DAQ Device Programming Guide` to `WPC Python Device Driver Programming Guide`
- Uniform name to `WPC Python device driver` in project.

v0.0.15 Date: 2022/09/05, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add `Material` folder in GUI example code
- Add package `wpcEXEbuild` requirement in `wpcsys`
- Add `How to build your own Python code to EXE file` in wiki

### Changed
- Change `Material` path
- Change author_email to wu@wpc.com.tw in PyPI `wpcsys` package

v0.0.14 Date: 2022/09/01, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add LICENSE, MANIFEST.in and setup.py in order to deliver `wpcsys` in PyPI
- Add `about` , `Quick Start`, `Requirements` and `License` in Readme.md
- Add `USB-DAQ-F1-RD.JPG` in Reference/Pinouts folder
- Add `Temperature-RTD` & `Temperature-TC` & `AI` & `AO` folder in order to create README file
- Add README.md in `System` & `AI` & `AIO` & `AO` & `DIO` & `Temperature-RTD` & `Temperature-TC` example console folder

### Changed
- Change WPC Python Version from `pywpc-0.2.1` to `pywpc-0.2.3`
- In version 0.2.1.1:
  - 0: Major revision (incompatible API change)
  - 2: Minor revision (maybe reconstruct architecture)
  - 1: Change driver source code
  - 1: Change Sphinx code
- Change API name `example_AI_N_samples_get_progressively` to `example_AI_N_samples_in_loop`

### Removed
- Remove Temperature folder
- Remove `system` import path and import `from wpcsys import pywpc`

v0.0.13 Date: 2022/08/30, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add GUI example code : Example_thermocouple, Example_RTD, Example_analog_input_on_demand, Example_I2C, Example_SPI
- Add WPC_DAQ_Devices_User_Manual_r17
- Add README.md in `I2C` & `SPI` & `UART` & `DIO` & `CAN` & `RTD` example console folder
- Add description in example code
- Add 25C08C.JPG & 25LC640.JPG in `Pinouts` folder
- Add `Datasheet` folder in `Reference` folder
- Add 24C08C.pdf & 25LC640.pdf in `Datasheet` folder
- Add `RTD` & `TC` folder in `Temperature` folder

### Changed
- Change WPC Python Version from `pywpc-0.2.0` to `pywpc-0.2.1`
- Renamed case-sensitive folder

### Removed
- Remove WPC_DAQ_Devices_User_Manual_r16

v0.0.12 Date: 2022/08/23, Developer: Chunglee_people
----------------------------------------------------
### Added
- Add example code packet classification
- Add GUI example code : Example_analog_output, Example_UART

### Changed
- Change WPC Python Version from `pywpc-0.1.19` to `pywpc-0.2.0`
- Change folder name `Example_AI_streaming` to `Example_analog_input`
- Change folder name `System` to `System_Network`

v0.0.11 Date: 2022/08/17, Developer: Chunglee_people
----------------------------------------------------
### Removed
- Remove unnecessary files

v0.0.10 Date: 2022/08/17, Developer: Chunglee_people
----------------------------------------------------
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
