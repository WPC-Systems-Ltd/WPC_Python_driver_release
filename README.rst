WPC Python Driver
=================

.. image:: https://img.shields.io/badge/pip%20install-wpcsys-orange.svg
   :target: https://pypi.org/project/wpcsys/
   :alt: pip install

.. image:: https://img.shields.io/pypi/v/wpcsys
   :target: https://pypi.org/project/wpcsys/
   :alt: PyPI

.. image:: https://img.shields.io/badge/Python-3.8%20to%203.12%20-blue.svg
   :target: https://pypi.org/project/wpcsys/
   :alt: Python version

.. image:: https://img.shields.io/badge/os-Ubuntu%20&%20Windows%2010-brown.svg
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
   :alt: Wheel support

Overview
--------

**WPC Python driver** is an easy-to-use open-source API for beginners and professionals.
It simplifies communication with WPC products using a consistent and intuitive interface.

With rich examples and simple logic—just ``open``, ``read/write``, and ``close``—you can easily access or update data.
It is a practical tool for both learning and developing applications with real-world hardware.

> **⚠️ Note:** Please ensure your firmware version is up-to-date to maintain compatibility.

Architecture
------------

The driver supports both **synchronous** and **asynchronous** operation:

- **Synchronous**: Executes tasks step-by-step, blocking until each completes.
- **Asynchronous**: Runs tasks independently, allowing concurrency and scalability.

Synchronous APIs are easier to understand and debug, while asynchronous APIs are ideal for high-performance applications.

Install and Upgrade
-------------------

Install via pip:

.. code-block:: shell

   pip install wpcsys

To install without dependencies:

.. code-block:: shell

   pip install wpcsys --no-deps

To upgrade:

.. code-block:: shell

   pip install --upgrade wpcsys

Supported Platforms
-------------------

This package provides prebuilt binaries (.so / .pyd) for:

+----------------+-----------------------+----------------+-----------------------------+
| Python Version | Platform              | File Format    | Supported WPC Products      |
+================+=======================+================+=============================+
| 3.8 ~ 3.12     | x86_64 Linux          | ``.so``        | All WPC products supported  |
+----------------+-----------------------+----------------+-----------------------------+
| 3.8 ~ 3.12     | Windows (win_amd64)   | ``.pyd``       | All WPC products supported  |
+----------------+-----------------------+----------------+-----------------------------+
| 3.8 ~ 3.12     | aarch64 Linux         | ``.so``        | **Drone products only**     |
+----------------+-----------------------+----------------+-----------------------------+

> **⚠️ Warning:** `aarch64-linux-gnu` builds support **only WPC drone products**.\
> Use with other products may cause errors or unexpected behavior.

.. warning::

   ``aarch64-linux-gnu`` builds support **only WPC drone products**.
   Use with other products may cause errors or unexpected behavior.

Quick Start
-----------

A minimal working example:

.. code-block:: python

   from wpcsys import pywpc

   print(pywpc.PKG_NAME)
   print(pywpc.HANDLE_LIST)

Example output of `HANDLE_LIST`:

::

   ['DeviceFinder', 'Drone', 'EthanA', 'EthanA2', 'EthanD', 'EthanEXD', 'EthanI', 'EthanIA',
    'EthanL', 'EthanO', 'EthanP', 'EthanT', 'USBDAQF1D', 'USBDAQF1DSNK', 'USBDAQF1AD',
    'USBDAQF1AOD', 'USBDAQF1TD', 'USBDAQF1RD', 'USBDAQF1CD', 'WifiDAQE3A', 'WifiDAQE3AH',
    'WifiDAQF4A', 'WifiDAQE3AOD', 'STEM', 'EMotion', 'EDriveST']

Resources
---------

- `GitHub Repository <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release>`_
- `Documentation <https://wpc-systems-ltd.github.io/WPC_Python_driver_release/>`_
- `Useful Conda Commands <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/Useful-Conda-Commands>`_
- `Run Examples in Console <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console>`_
- `Build EXE from Python Code <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-build-your-own-Python-code-to-EXE-file>`_
- `Install Miniconda and Create Virtual Env <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment>`_
- `LabVIEW Run-Time Engine <https://drive.google.com/file/d/1Uj6r65KhNxvuApiqrMkZp-NWyq-Eek-k/view>`_

License
-------

Licensed under the MIT License. See `LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE>`_ for details.
All included components allow for both commercial and non-commercial use.
