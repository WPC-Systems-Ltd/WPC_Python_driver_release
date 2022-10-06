from setuptools import setup, find_packages
from platform import python_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

## --- get release version ---
release_version = "unknown"
with open("wpcsys/version.py") as f:
    line = f.read().strip()
    release_version = line.replace("version = ", "").replace('"', '')


## --- get python version ---
py_ver = python_version()
if py_ver == "3.10.4":
    python_requires = '==3.10.*'
    release_version = release_version + ".1"
if py_ver == "3.9.0":
    python_requires = '==3.9.*'
    release_version = release_version + ".2"
if py_ver == "3.8.0":
    python_requires = '==3.8.*'
    release_version = release_version + ".3"   

setup(
    name= "wpcsys",
    version= release_version,
    description='WPC Device Driver Python API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="chunglee_people",
    author_email="wu@wpc.com.tw",
    url="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release",
    packages=['wpcsys'],
    include_package_data=True,
    license='MIT',
    install_requires=['pyusb>=1.2.1', 'numpy>=1.23.0',
                      'qasync>=0.23.0', 'matplotlib>=3.5.2', 'qasync>=0.23.0', 'PyQt5Designer>=5.14.1',
                      'PyQt5>=5.15.4', 'PyQt5-Qt5>=5.15.2', 'PyQt5-sip>=12.10.1', 'wpcEXEbuild>=0.0.1'],
    keywords='wpc, daq, driver, usb, ethernet, wifi, data acquisition',
    python_requires = python_requires,
)
