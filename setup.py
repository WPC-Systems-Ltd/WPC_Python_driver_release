from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name= "wpc",
    version="0.2.2",
    description='WPC Python API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="chunglee_people",
    author_email="lschung@wpc.com.tw",
    url="https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release",
    packages=['wpc'],
    include_package_data=True,
    license='MIT',
    install_requires=['pyusb>=1.2.1', 'numpy>=1.23.0',
                      'qasync>=0.23.0', 'matplotlib>=3.5.2', 'qasync>=0.23.0', 
                      'PyQt5>=5.15.7', 'PyQt5-Qt5>=5.15.2', 'PyQt5-sip>=12.11.0'],
    keywords='DAQ, usb, driver, wifi',
    python_requires=">=3.10",
)
