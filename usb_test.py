import sys
import os
import usb.backend.libusb1 as libusb1

def getLibUSB1():
    dir_path = os.path.dirname(__file__)
    print(dir_path)

    ## Scenerio 1
    ## Location of library in WPC_Python_driver_release
    path = f'{dir_path}/libusb-1.0.dll'
    backend = libusb1.get_backend()
    print(backend)

    # ## Scenerio 2
    # path = 'd:/Chunglee_WPC/WPC_Python_driver_release/ext_lib/libusb-1.0.dll'
    # backend = libusb1.get_backend(find_library=lambda x: path)
    # print(backend)

    ## Location of library in WPC_Python_driver_source
    if backend is None:
        path = f'{dir_path}/../ext_lib/libusb-1.0.dll'
        backend = libusb1.get_backend(find_library=lambda x: path)

    if backend is None:
        print("ExtLibNotFoundWarning")
    return backend

def main():
    getLibUSB1()
    return
if __name__ == '__main__':
    main()