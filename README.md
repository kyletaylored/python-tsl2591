# TSL2591 Python Library

[![GitHub stars](https://img.shields.io/github/stars/kyletaylored/python-tsl2591.svg)](https://github.com/kyletaylored/python-tsl2591/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kyletaylored/python-tsl2591.svg)](https://github.com/kyletaylored/python-tsl2591/network)
[![GitHub issues](https://img.shields.io/github/issues/kyletaylored/python-tsl2591.svg)](https://github.com/kyletaylored/python-tsl2591/issues)
[![Inspired by Adafruit](https://img.shields.io/badge/Inspired%20by-adafruit-blue.svg)](https://gitgud.io/adafruit/Adafruit_TSL2591_Library)
[![Build Status](https://travis-ci.org/kyletaylored/python-tsl2591.svg?branch=master)](https://travis-ci.org/kyletaylored/python-tsl2591)

This is a simple python library for the Adafruit TSL2591 breakout board based on the [Arduino library](https://github.com/adafruit/Adafruit_TSL2591_Library) from Adafruit. It was developed to work on a Raspberry PI.

## Requirements
To use this library, you must have the following:
1. TSL2591 sensor (__not__ the [TSL25**61**](https://www.adafruit.com/product/439))
2. I2C enabled device
3. Python 3 (though Python 2 should technically still work)

## Installation

This module can be installed using pip (and can find a copy of this module on [PyPi](https://pypi.org/project/python-tsl2591/)).

```bash
pip install python-tsl2591
```

### Quickstart
This library comes with an example file you can use, or you can copy and paste the following:

```python
from python_tsl2591 import tsl2591
import time

if __name__ == '__main__':

    tsl = tsl2591()  # initialize
    # full, ir = tsl.get_full_luminosity()  # Read raw values (full spectrum and infared spectrum).
    # lux = tsl.calculate_lux(full, ir)  # Convert raw values to Lux.

    while True:
        print(tsl.get_current()) # Return object with all values.
        # print (lux, full, ir)
        time.sleep(2)
```

### Install from Source

You can also install this Python module from source:

```bash
git clone https://github.com/kyletaylored/python-tsl2591
cd python-tsl2591
python setup.py install
```

## Enabling I2C on your Raspberry Pi

You can enable I2C on the Raspberry Pi by following the instructions on [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c).

The quick version is:

1. Run `sudo raspi-config`
2. Select `Advanced Options`
3. Enable I2C
4. Reboot (`sudo reboot`)

When testing I2C (`sudo i2cdetect -y 1`), you should see at least one connected device, your TSL2591 at `0x29`. For more information, see the [FAQ](#i2c-check-for-static-address).

## FAQ

### Fatal error (deprecated)

**UPDATE**: We have integrated the `smbus2` library, which is an smbus library built in Python, and does not require any system packages like `smbus-cffi` or `libffi-dev`.

If you do not have those Raspbian packages installed prior to installing this library, you will run into errors that look similar to this.

```
fatal error: ffi.h: No such file or directory
     #include <ffi.h>
                     ^
compilation terminated.
error: command 'arm-linux-gnueabihf-gcc' failed with exit status 1
```

### I2C Check for Static Address

Because the TSL2591 connects via I2C, it's always good to run the I2C detection to verify the address is being read. Unlike the TSL2561 with programmable addresses, the TSL2591's address is hard coded and cannot be changed - thus it will always show `0x29`.

In the example output below, you can see there are two I2C devices detected, one being the TSL2591.

```bash
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- 29 -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

## License

Python files in this repository are released under the [MIT license](LICENSE.md).
