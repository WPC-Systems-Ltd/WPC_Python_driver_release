Overview
--------

**WPC Python driver**, also known as `pywpc`, contains APIs for interacting with basically WPC DAQ cards or any other WPC USB, WiFi and Ethernet based devices.
It supports Python version from 3.8 to 3.10 under Windows 10 operating systems.

Our APIs support synchronous and asynchronous modes for computer processes or threads.

Synchronous mode means that two or more processes run in a step-by-step manner, one after the other.In this mode, the execution of a process is blocked until the previous process is completed.

Asynchronous mode means that processes run independently of each other and don't wait for the completion of the previous process. Instead, each process runs on its own, without blocking the execution of other processes.

In general, synchronous mode is easier to understand and debug, while asynchronous mode is more scalable and allows for greater concurrency.

Some API functions in the `pywpc` package may not compatible with earlier versions of WPC DAQ firmware.
To update device firmware to the latest version, please use WPC Device Manager and `LabVIEW Run-time engine <https://drive.google.com/file/d/1Uj6r65KhNxvuApiqrMkZp-NWyq-Eek-k/view>`_.
You can download WPC Device Manager by `latest release <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/releases/tag/v2.0.0>`_ or visit `WPC Systems Ltd. official website <http://www.wpc.com.tw/>`_.


+-------------------+-----------------------------------------------------------------------------------+
|                   | Link                                                                              |
+===================+===================================================================================+
| WPC official site | http://www.wpc.com.tw/                                                            |
+-------------------+-----------------------------------------------------------------------------------+
| GitHub            | https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release                      |
+-------------------+-----------------------------------------------------------------------------------+
| User guide        | https://wpc-systems-ltd.github.io/WPC_Python_driver_release/                      |
+-------------------+-----------------------------------------------------------------------------------+
| Example code      | https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples   |
+-------------------+-----------------------------------------------------------------------------------+

.. image:: https://img.shields.io/badge/pip%20install-wpcsys-orange.svg
    :target: https://pypi.org/project/wpcsys/
    :alt: pip install

.. image:: https://img.shields.io/pypi/v/wpcsys
    :target: https://pypi.org/project/wpcsys/
    :alt: PyPI

.. image:: https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10-blue.svg
    :target: https://pypi.org/project/wpcsys/
    :alt: Python

.. image:: https://img.shields.io/badge/os-Windows%2010-brown.svg
    :target: https://www.microsoft.com/zh-tw/software-download/windows10
    :alt: OS

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License: MIT

.. image:: https://img.shields.io/badge/docs-passing-green.svg
    :target: https://wpc-systems-ltd.github.io/WPC_Python_driver_release/
    :alt: docs

.. image:: https://img.shields.io/pypi/wheel/wpcsys
    :target: https://pypi.org/project/wpcsys/
    :alt: Wheel

.. note::

   Make sure the latest version of firmware is up to date with your products.

Quick Start
-----------
**Easy, fast, and just works!**

   >>> from wpcsys import pywpc
   >>> pywpc.PKG_NAME
   pywpc
   >>> pywpc.__version__
   2.0.1
   >>> pywpc.HANDLE_LIST
   ['DeviceFinder', 'DataLogger', 'WifiDAQE3A', 'EMotion', 'EthanA', 'EthanD', 'EthanL', 'EthanO', 'USBDAQF1D', 'USBDAQF1DSNK', 'USBDAQF1AD', 'USBDAQF1AOD', 'USBDAQF1TD', 'USBDAQF1RD', 'USBDAQF1CD']

Install and Upgrade
-------------------

- Install

.. code-block:: shell

   pip install wpcsys

- Upgrade

.. code-block:: shell

   pip install --upgrade wpcsys

Requirements
------------
Python 3.8 or later with all `requirements.txt <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/requirements.txt>`_ dependencies installed, including PyQt5, PyQt5Designer, qasync and so on.

.. code-block:: shell

   pip install -r requirements.txt

Products
--------
Ethernet based motion card

- EMotion

Ethernet based DAQ card

- Ethan-A

- Ethan-D

- Ethan-L

- Ethan-O

USB interface DAQ card

- USB-DAQ-F1-D (Digital)

- USB-DAQ-F1-DSNK (24V Digital)

- USB-DAQ-F1-AD (Digital + AI)

- USB-DAQ-F1-TD (Digital + Thermocouple)

- USB-DAQ-F1-RD (Digital + RTD)

- USB-DAQ-F1-CD (Digital + CAN)

- USB-DAQ-F1-AOD (Digital + AI + AO)

Wifi based DAQ card

- Wifi-DAQ-E3-A

I/O Function Table
------------------

+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Model          |AI |AO |DI        |DO        |CAN |UART |SPI  |I2C  |RTD |TC |Motion|
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Emotion        |   |   |          |          |    |     |     |     |    |   |0     |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Ethan-A        |0  |   |          |          |    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Ethan-D        |   |   |1         |0         |    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Ethan-L        |   |   |          |0         |    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Ethan-O        |   | 0 |          |          |    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-D   |   |   |0, 1, 2, 3|0, 1, 2, 3|    |1, 2 |1, 2 |1, 2 |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-DSNK|   |   |0, 1      |      2, 3|    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-AD  |0  |   |0, 1, 2, 3|0, 1, 2, 3|    |1, 2 |2    |1, 2 |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-TD  |   |   |0, 1, 2, 3|0, 1, 2, 3|    |1, 2 |2    |1, 2 |    |1  |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-RD  |   |   |0, 1, 2, 3|0, 1, 2, 3|    |1, 2 |2    |1, 2 |1   |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-CD  |   |   |0, 1, 2, 3|0, 1, 2, 3|1   |1, 2 |2    |1, 2 |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| USB-DAQ-F1-AOD |0  |0  |0, 1, 2, 3|0, 1, 2, 3|    |1, 2 |     |1, 2 |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+
| Wifi-DAQ-E3-A  |1  |   |          |          |    |     |     |     |    |   |      |
+----------------+---+---+----------+----------+----+-----+-----+-----+----+---+------+

Remark: `TC` stands for `Thermocouple`

Take `USB-DAQ-F1-AOD` for example:

- Port 0 is available for AI

- Port 2 is available for DI

- Ports 0 & 1 are available for DO

- Port 2 is available for UART

References
----------
- `Useful conda commands <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/Useful-Conda-Commands>`_

- `User manual - WPC Python driver <https://wpc-systems-ltd.github.io/WPC_Python_driver_release/>`_

- `Run example code in console <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console>`_

- `How to build your own Python code to EXE file <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-build-your-own-Python-code-to-EXE-file>`_

- `How to install miniconda and build your own virtual environment <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment>`_

License
-------

**WPC Python driver release** is licensed under an MIT-style license see `LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE>`_ Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.
