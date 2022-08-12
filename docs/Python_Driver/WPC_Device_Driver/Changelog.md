WPC_Device_Driver Version Changelog
===================================


Unreleased
----------

### TODO
- Find USB devices in broadcast
- Verify DIO modules functions, except for `setSlotDI` & `setSlotDO`

v0.1.18 Date: 2022/08/10, Developer: Chunglee_people
----------------------------------------------------

### Added 
- Add `checkFuncPinMap` & `checkPinMap` function in WPC_utilities
- Add complete pinmap in function modules
- Use dictionary to get or check port in function modules
- Check pin state in function modules when open function

### Fixed 
- Fix pinstate order in `Sys_getPinModeInPort`
- Fix `idle` to `Idle` &  `disabled` to `Disabled` in pin_mode_dict

### Remove 
- Remove port list in function modules

v0.1.17 Date: 2022/08/09, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add Thermo example code (#35)
  - `Temperature/example_RTD_read_channel_data.py`
  - `Temperature/example_RTD_read_channel_status.py`
- Add UART, I2C and SPI pinmap

### Changed
- Change example code name from
  - `example_Thermo_read_channel_status` to `example_TC_read_channel_status` 
  - `example_Thermo_read_channel_data` to `example_TC_read_channel_data` 
- Change folder name from `Thermo` to `Temperature`

v0.1.16 Date: 2022/08/04, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add AO example code (#41)
  - `AIO/example_AO_write_one_channel.py`
  - `AIO/example_AO_write_all_channels.py`
  - `AIO/example_AIO_one_channel_loopback.py`
  - `AIO/example_AIO_all_channels_loopback.py`
- Add SPI example code (#46)
  - `SPI/example_SPI_read_and_write.py`
  - `SPI/example_SPI_write.py`
- Add I2C example code (#47)
  - `I2C/example_SPI_write_and_read.py` 
- Add Error class 
  - `SPIModeNotVaildError`
- Add `I2C` in LABEL_DICT
- Add API `DO_getPinMap` & `DI_getPinMap` in DIOModule class
- Add API `SPI_getPort` & `I2C_getPort` & `CAN_getPort` & `UART_getPort` & 
`Thermal_getPort` & `AO_getPort` & `AI_getPort` in its class
 
### Changed
- Changed `CAN bus` to `CAN` in LABEL_DICT
- Changed API name `AO_writeByChannels` to `AO_writeOneChannel`
- Changed API name `AO_writeSynchronized` to `AO_writeAllChannels`
- Changed API name `DO_writeValuePins` to `DO_writePins`
- Changed API name `DO_writeValuePort` to `DO_writePort`
- Changed API name `I2C_setFrequency` to `I2C_setClockRate`
- Changed API name `_checkI2CFrequency` to `_checkI2CClockRate` 
- Changed class name `ThermalCoupleModule` to `ThermocoupleModule` 

### Fixed
- Fixed `WPC_devices.USBDevice.__init_` execute two times in USBDAQF1AOD class

### Remove
- Remove Error class `SPICPOLNotVaildError` & `SPICPHANotVaildError`
- Remove `ThermocoupleModule` class in USBDAQF1RD

v0.1.15 Date: 2022/08/01, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add product: USBDAQF1CD & USBDAQF1AD & USBDAQF1RD
- Add __init__ in I2CModule and SPIModule to get port list
- Add I2C & SPI port defination in individual WPC products
- Add USBDAQF1RD class in WPC_products.py
- Add `CANModule` & `AOModule` function
- Add CANFrame class
- Add I2CModule & SPIModule
- Add CAN example code (#40)
  - `CAN/example_CAN_read.py`
  - `CAN/example_CAN_write.py`
- Add Error class 
  - `CANPortNotAvaliableError` 
  - `CANSpeedNotVaildError`
  - `CANTXNotVaildError`
  - `AOPortNotAvaliableError`
  - `AOModeNotVaildError`
  - `AOSpanNotVaildError`
  - `AOChannelNotAvaliableError`
  - `AIModeNotAvaliableError`
  - `InputDataNotInRangeError` 
  - `I2CPortNotAvaliableError`
  - `I2CClockNotSupportError`
  - `I2CAddressSizeNotVaildError`
  - `SPIPortNotAvaliableError`
  - `SPIDataLengthExceedMAXError`
  - `SPIDataSizeNotVaildError`
  - `SPIFirstBitNotVaildError`
  - `SPIPrescalerNotVaildError`
  - `SPICPOLNotVaildError`
  - `SPICPHANotVaildError`
- Add waring class (#42)
  - `UARTQueueOverflowWarning` 
  - `CANQueueOverflowWarning`
  - `AIQueueOverflowWarning`
- Add `_checkAIMode` & `checkEachItemInRange` & function
- Add trace code in warning class (#42)

### Fixed
- Fixed non-blocking acquire when called `_closeCAN` and `_closeUART`
- Fix UART streaming command judgement when put data in queue
- Bug of missing port `CAN_stop` inside `CAN_close`
- Replace `Depend on` with `According to` in function description
- Bug of missing `_closeUART` if WPC Device product has `UARTModule`.

### Remove
- Remove argument param `port` in WifiSystemModule
- Remove default argument param `port` in `CANModule` & `ThermalCoupleModule` &`ThermalModule`  
- Remove `_openAI_Wifi` & `_closeAI_Wifi` in `WifiDAQE3A`

v0.1.14 Date: 2022/07/25, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add product: USBDAQF1TD
- Add ThermalCoupleModule
- Add UART example code (#36)
  - `UART/example_UART_read.py`
  - `UART/example_UART_write.py`
- Add Thermo example code (#35)
  - `Thermo/example_Thermo_read_channel_data.py`
  - `Thermo/example_Thermo_read_channel_status.py`
- Add Error code 
  - `ThermalPortNotAvaliableError` 
  - `ThermalChipSelectNotAvaliableError`
  - `ThermalModeNotVaildError` 
  - `ThermalTypeNotVaildError`
  - `UARTPortNotAvaliableError`
  - `UARTExceedMaxLengthError`
  - `UARTBaudRateNotSupportError`

- Add html source to `WPC_python_Driver_Release`
- Add `thread` and `data_pool_strm2` for port2 in USBDevice
- Hide `_UART_startReading` and release new API `UART_read` for user

### Changed
- Change variable or function function name which contained  `spi_index` to `port`
- Change variable or function function name which contained  `chip_select` to `channel`
- Generate sphinx in `WPC_python_Driver_Release`'s example code
- Change `General` to `System` in EXAMPLE_DICT
- Change `wireless device` to `WIFI` in LABLE_DICT

### Remove
- Remove example code in WPC_Device_Driver

v0.1.13 Date: 2022/07/19, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add Thermo modules function
- Add UART modules function
- Add DIO pinmap
- Add DIO modules function decriptions
- Add DIO example code (#32)
  - `DIO/example_DIO_loopback_pins.py`
  - `DIO/example_DIO_loopback_port.py`
  - `DIO/example_DO_write_pins.py`
  - `DIO/example_DO_write_slot.py` 
  - `DIO/example_DO_blinky_pins.py` 
  - `DIO/example_DO_blinky_port.py`
- Add AIO example code (#19)
  - `AIO/example_AI_on_demand_once.py`
- Add General example code 
  - `General/example_get_pin_mode.py`
- Add `Tutorial` in exmaple dictionary
  - `Tutorial/example_multiple_loops_async.py`
  - `Tutorial/example_multiple_loops_thread.py`
  - `Tutorial/example_single_loop_async.py`
  - `Tutorial/example_single_loop_thread.py`
- Add DIO function
  - `DO_openPort` & `DO_writeValuePort` & `DO_closePort` & `DO_openPins` & `DO_writeValuePins` & `DO_closePins`
  - `DI_openPort` & `DI_readPort` & `DI_closePort` & `DI_openPins` & `DI_readPins` & `DI_closePins`
  - `_checkDIPort` & `_checkDOPort` & `_checkDIPortAndPin` & `_checkDOPortAndPin`& `_getPinIndexInList`
- Add type convert function 
  - `convertPinIndexAndBooltoInt` & `convertPinIndextoInt` & `convertBinary`
- Add type check function 
  - `checkInputType` & `checkInputTypeConsistent`
- Add Error code 
  - `PinsNotExistError` 
  - `PinsValueNotDefineError`
  - `InputTypeNotCosisitentError` 
  - `InputTypeNotCorrectError`
  - `DIPortNotAvaliableError`
  - `DOPortNotAvaliableError`
  - `AIPortNotAvaliableError`
 
### Changed
- Change class name from `WifiDAQ` to `WifiDAQE3A` 
- Change variable or function function name which contained  `slot`  to `port`
- Change DIO parameter name `connector` to `port`
- Change example name `example_get_basic_device_info.py` to `example_get_device_info.py`
- Change example name `example_AI_N_samples_get_at_once.py` to `example_AI_N_samples_once.py`
- Change example dictionary name `basic` to `General`
- Change example dictionary name `AI` to `AIO`

### Fixed
- Bug of missing handle in `loop_onDemand` in `example_AI_on_demand_in_loop.py`
- In setRTCDateTime function, fix prototype input from str to 6 int
- `shutil.rmtree(path, True)`, the second function parameters to `True`
- Fix output mac address with 2 digits. From `%x`to`%02x`
- Fix `setDIOCurrent` to `_setDIOCurrent`
- Fix `readAndGetDI`  to `_readAndGetDI`
- Fix `toggleAndWriteDO`  to `_toggleAndWriteDO`
- Fix `DI_readPins` return list with mask

### Remove
- Wifi DAQ AI wrapper function

v0.1.12 Date: 2022/06/30, Developer: Chunglee_people
-----------------------------------------

### Added
- Add example codes: (#19)
  - `basic/example_single_loop_async.py`
  - `basic/example_single_loop_thread.py`
  - `basic/example_multiple_loops_async.py`
  - `basic/example_multiple_loops_thread.py`
  - `AI/example_AI_N_samples_get_at_once.py`
  - `AI/example_AI_N_samples_get_progressively.py`

### Fixed
- Bug of missing connector in `__init__` in `USBDAQF1AOD`
- Bug of wrong variable name in `BcstDevice.close`

### Removed
- In BcstModule, remove the input parameters of `broadcast=True` in `getDeviceInfo` & `checkMACAndSetIP` & `checkMACAndReboot` function.
 

v0.1.11 Date: 2022/06/28, Developer: Linc
-----------------------------------------

### Added
- New classes: `USBClient` & `USBDevice` (#4)
- Test code: `dev_USB.py`
- Mechanism to remove `.rst` in `python setup.py clean` (#27)
- Commands: `OPEN_AI` & `CLOSE_AI`
- Mechanism to ensure disconnection before closure
- Mechanism to avoid breakdown when `connect`, `disconnect`, or `close` are called multiple times

### Changed
- Improved `setup.py merge` to avoid bug (#27)
- Added `connector` to `AIModule` APIs' arguments
- Renamed `byte_str` to `binary_str`
- Renamed `wifi_analog_signal` to `ai_signal_queue`
- Renamed `open` to `connect`
- Renamed `close` to `disconnect`
- Renamed `free` to `close`
- Moved TCP & UDP parameters to `WPC_clients.py`
- Generalized `_getStreamingFromPool` for all streaming commands

### Fixed
- Bug of defining USB products as ETH devices
- Bug in `_splitPacket` function


v0.1.10 Date: 2022/06/24, Developer: Chunglee_people
----------------------------------------------------

### Added
- Add `BcstDevice` class(#23)
- Add `BcstModule` class(#23)
- Add `Broadcaster` class(#23)
- Add `AI` folder in `examples/`
- Add `WarningRemind` class (#22)
- Add overflow warning in `_splitAIDataThread` (-50003, The AI queue is overflow) (#21)
- Add `openAI` & `closeAI` & `freeAI` in `AIModule` (#20)
- Add example codes: (#19)
  - `AI/example_AI_continuous.py`
  - `AI/example_AI_on_demand_in_loop.py`
  - `basic/example_Broadcasts.py`
  - `basic/example_web_device_info.py`
  - `basic/example_WIFI_DAQ_status.py`
- Add queue arguments to `split_ai_data_thread`
- Add command `0x6F READ_ACCELERATION`
- Add ip address with inital value `None` in device class.
- Add message `None` in `self.data_pool_strm` queue when closed.

### Changed
- Changed `.rst` file structure & autogen in `setup.py`
- Changed span to -5 ~ +5
- Changed command (0xBB) name `CHECK_BUFFER_REMAIN` to `CHECK_BUFFER_STATUS`
- Moved `split_ai_lock` & `split_ai_data_thread` & `wifi_analog_signal` to `AIModule` (#20)

### Removed
- Remove `example_Wifi_DAQ_OnDemand.py`
- Remove `raw_ai_queue` (#20)

v0.1.9 Date: 2022/06/18, Developer: Linc
----------------------------------------

### Added
- `setup.py`:
  - Mechanism to parse block comments
  - Automatic creation of `.rst` files
  - Automatic creation of documentation
  - Automatic creation of distribution (lib + examples + docs) (#17)
  - Automatic incrementation of distribution folder name (#17)
  - Added `verbose` option to save functions (#24)
- `WPC_config.py`:
  - `PKG_NAME` as package name
  - `PKG_FULL_NAME` as package descriptive name
  - `PRODUCT_DICT` as dictionary for product details (characteristics & resource map)
  - `EXAMPLE_DICT` as dictionary for example code details
  - `LABEL_DICT` as dictionary for label-mapping
- `WPC_packets.py`:
  - Dev-only API: `getDriverInfo_dev`
- `WPC_devices.py`:
  - Added `verbose` option to device init, open, close, & free (#24)
- Others:
  - Some example documentations

### Changed
- Turned dev-only APIs into private functions (#18)
- Prototype of `getDriverInfo`
- Reorganized `.rst` files

### Removed
- `checkOnDemand`


v0.1.8 Date: 2022/06/16, Developer: Linc
----------------------------------------

### Added
- New file: `setup.py` for compiling `.pyd` file
- New file: `pywpc.py` to simplify importations for developers
- New file: `WPC_config.py` for defining what is publicly visible
- Added `examples/` folder
- Script to merge all sources files into one
- Script to convert `.py` into `.pyd`
- Script to generate documentations

### Changed
- Added `pywpc/` to `.gitignore`
- Updated script usage to `README.md`
- Renamed `driver/` to `src/`
- Moved example files to `examples`

### Fixed
- Typo error on `USBDAQF1AOD`


v0.1.7 Date: 2022/06/16, Developer: Chunglee_people
---------------------------------------------------

### Added
- Add new API for onDemand `readAIOnDemand`
- Add new example code for `example_System`
- Add close message `None` to queue when close exe
- Set wifi_analog_signal queue size to `1000000`
- Set wifi_analog_signal queue timeout to `999999`

### Changed
- Rename example code `example_Wifi_DAQ.py` to `example_Wifi_DAQ_OnDemand.py`
- Rename `getAIStreamingData` to `readAIStreaming`


v0.1.6 Date: 2022/06/09, Developer: Linc
----------------------------------------

### Added
- Retry mechanism
- Function to determine command type
- Handle multiple replies from UDP broadcast


v0.1.5 Date: 2022/06/09, Developer: Chunglee_people
---------------------------------------------------

### Fixed
- AI data split & reconstruction algorithm
- Fix API `getAIStreamingData`
- Fix API `getStreamingFromPool`


v0.1.4 Date: 2022/06/08, Developer: Linc
----------------------------------------

### Added
- Thread for UDP reception
- Added `TCPClient` & `UDPClient` classes

### Changed
- Renamed: `WPC_TCP.py` => `WPC_clients.py`
- Renamed `Client` class to `WebClient`


v0.1.3 Date: 2022/06/07, Developer: Chunglee_people
---------------------------------------------------

### Added
- Test for AI receiving packets and split it with asynchronous structure (not yet)


v0.1.2 Date: 2022/06/01, Developer: Chunglee_people
---------------------------------------------------

### Added
- Completed 0xEX packets
- UDP broadcast in device class


v0.1.1 Date: 2022/05/31, Developer: Chunglee_people
---------------------------------------------------

### Added
- Completed 0x7X and 0xFX packets

### Notes
- StartAI will not execute code (need to wait thread for streaming)


v0.0.2 Date: 2022/05/28, Developer: Linc  
---------------------------------------------------

### Added
- New file: `WPC_utilities.py`
- New file: `WPC_errors.py`
- New file: `WPC_products.py`
- New file: `example_Ethan.py`
- Defined type conversion functions
- Defined hierarchical classes for different devices
- Defined classes for each product using inheritance
- Defined classes for different modules
- New fct: `echoPacket` as the base function for all packets to send

### Changed
- Renamed: `WPC_CMD.py` => `WPC_commands.py`
- Renamed: `WPC_Packet.py` => `WPC_packets.py`
- Renamed: `WPC_Device.py` => `WPC_devices.py`
- Renamed: `main.py` => `example_Wifi_DAQ.py`
- Moved all driver files to `driver/`
- Separated error's code & message

### Notes
- `example_Ethan.py` is guaranteed to be workable.
- It is served as an example of how we should transform codes.


v0.0.1 Date: 2022/05/27, Developer: Chunglee_people
---------------------------------------------------

### Added
- async wifi function