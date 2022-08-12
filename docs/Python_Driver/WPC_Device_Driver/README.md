WPC_Device_Driver
=================

`pywpc` is a Python-based driver for WPC devices.

This page is served as an application note for developers.


Package requirement
-------------------

Install packages required for building:
```
$ pip install cpython sphinx sphinx-rtd-theme numpydoc
```
Install packages required for running:
```
$ pip install numpy pyusb
```


Build
-----

### Build all

```
$ python setup.py
```

### Individual build

Merge to a single source file into `build`:
```
$ python setup.py merge
```
Compile a `.pyd` library into `pywpc`:
```
$ python setup.py lib
```
Clean documentations and regenerate `.rst` files into `docs/source/`:
```
$ python setup.py clean
```
Generate documentations into `docs/build/html/`:
```
$ python setup.py docs
```
Make a distribution in `dist/`:
```
$ python setup.py dist
```

### Specific build

Update source and check library:
```
$ python setup.py merge lib
```
Update documentations and check it:
```
$ python setup.py merge docs
```
Check documentations after adding a new device or a new example:
```
$ python setup.py merge clean docs
```


Examples
--------

```
$ python examples/<category>/example_<name>.py
```
