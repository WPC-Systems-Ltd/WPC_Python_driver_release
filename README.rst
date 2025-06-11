Overview
--------
Welcome to **WPC Python driver** API documentation. It is an easy-to-use open-source tool for beginners.
We provide excellent example codes to help you quickly get started with our products, connecting code to real-world usage. This makes it a great way to learn.

Therefore, we highly recommend using our driver because it's simple to use. Just ``open``, ``read/write``, and ``close`` - allowing you to access or update data with ease.
Adding WPC Python driver to your toolkit not only simplifies tasks but also provides a practical learning experience that bridges theory and real-world application.

Last but not least, it's a valuable resource for both learning and working efficiently.

Architecture
------------
Our APIs support synchronous and asynchronous modes for computer processes or threads.

Synchronous mode means that two or more processes run in a step-by-step manner, one after the other.In this mode, the execution of a process is blocked until the previous process is completed.

Asynchronous mode means that processes run independently of each other and don't wait for the completion of the previous process. Instead, each process runs on its own, without blocking the execution of other processes.

In general, synchronous mode is easier to understand and debug, while asynchronous mode is more scalable and allows for greater concurrency.

.. image:: https://img.shields.io/badge/pip%20install-wpcsys-orange.svg
    :target: https://pypi.org/project/wpcsys/
    :alt: pip install

.. image:: https://img.shields.io/pypi/v/wpcsys
    :target: https://pypi.org/project/wpcsys/
    :alt: PyPI

.. image:: https://img.shields.io/badge/Python-3.8%20to%203.12%20-blue.svg
    :target: https://pypi.org/project/wpcsys/
    :alt: Python

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
    :alt: Wheel

.. note::

   Make sure the latest version of firmware is up to date with your products.

Install and Upgrade
-------------------

- Install

.. code-block:: shell

   pip install wpcsys

- Only install wpcsys

.. code-block:: shell

   pip install wpcsys --no-deps

- Upgrade

.. code-block:: shell

   pip install --upgrade wpcsys

Supported Platforms and Product Compatibility
---------------------------------------------

This module provides prebuilt binaries (.so / .pyd) for the following platforms and Python versions:

+----------------+-----------------------+----------------+-----------------------------+
| Python Version | Platform              | File Format    | Supported WPC Products      |
+================+=======================+================+=============================+
| 3.8 ~ 3.12     | x86_64 Linux          | ``.so``        | All WPC products supported  |
+----------------+-----------------------+----------------+-----------------------------+
| 3.8 ~ 3.12     | Windows (win_amd64)   | ``.pyd``       | All WPC products supported  |
+----------------+-----------------------+----------------+-----------------------------+
| 3.8 ~ 3.12     | aarch64 Linux         | ``.so``        | **Drone products only**     |
+----------------+-----------------------+----------------+-----------------------------+

.. warning::

   The Python build for ``aarch64-linux-gnu`` **only supports WPC Drone products**.
   Using it with other WPC products may result in unexpected behavior or incompatibility.

Please ensure that you use the correct binary for your platform and target application.


Quick Start
-----------
**Easy, fast, and just works!**

.. code-block:: console

   >>> from wpcsys import pywpc
   >>> pywpc.PKG_NAME
   pywpc
   >>> pywpc.HANDLE_LIST
   ['DeviceFinder', 'Drone', 'EthanA', 'EthanA2', 'EthanD', 'EthanEXD', 'EthanI', 'EthanIA', 'EthanL', 'EthanO', 'EthanP', 'EthanT', 'USBDAQF1D', 'USBDAQF1DSNK', 'USBDAQF1AD', 'USBDAQF1AOD', 'USBDAQF1TD', 'USBDAQF1RD', 'USBDAQF1CD', 'WifiDAQE3A', 'WifiDAQE3AH', 'WifiDAQF4A', 'WifiDAQE3AOD', 'STEM', 'EMotion', 'EDriveST']

References
----------
- `GitHub <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release>`_

- `Documentation - WPC Python driver <https://wpc-systems-ltd.github.io/WPC_Python_driver_release/>`_

- `Useful conda commands <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/Useful-Conda-Commands>`_

- `Run example code in console <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-run-WPC-Python-driver-example-code-in-console>`_

- `How to build your own Python code to EXE file <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-build-your-own-Python-code-to-EXE-file>`_

- `How to install miniconda and build your own virtual environment <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/wiki/How-to-install-miniconda-and-build-your-own-virtual-environment>`_

- `LabVIEW Run-time engine <https://drive.google.com/file/d/1Uj6r65KhNxvuApiqrMkZp-NWyq-Eek-k/view>`_

License
-------

**WPC Python driver** is licensed under an MIT-style license see `LICENSE <https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/blob/main/LICENSE>`_ Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.
