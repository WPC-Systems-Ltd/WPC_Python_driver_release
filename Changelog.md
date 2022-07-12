WPC_Device_Driver_Example_GUI Version Changelog
===================================



v0.0.3 Date: 2022/07/07, Developer: Chunglee_people
---------------------------------------------------
### Changed
- Change WPC Python Version from `pywpc-0.1.12` to  `pywpc-0.1.13` (templete, Need to verify)

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

v0.0.2 Date: 2022/07/01, Developer: Chunglee_people
---------------------------------------------------
### Changed
- Change WPC Python Version from `pywpc-0.1.10` to  `pywpc-0.1.12`

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
                                            
v0.0.1 Date: 2022/06/29, Developer: Chunglee_people
---------------------------------------------------
### Added
-  example GUI `UIexample_AIStreaming` & `UIexample_Broadcasts` & `UIexample_get_device_info`.
