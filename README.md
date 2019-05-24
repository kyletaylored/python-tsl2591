# TSL2591 python module

This is a simple python library for the Adafruit TSL2591 breakout board based on the [Arduino library](https://github.com/adafruit/Adafruit_TSL2591_Library) from Adafruit. It was developed to work on a Raspberry PI.

# INFO

Enabeling I2C on the Raspberry Pi. You should be fine by following the instruction on [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c).

In the last step ('Testing I2C') you should see at least one connected device, your TSL2591 (most likely at 0x29 ).

## Installing

Prior to using this library, you will need the following packages installed on your Raspberry Pi.

```bash
sudo apt-get install libffi-dev libssl-dev
sudo apt-get install python3-smbus
```

To install the python module download this repository and run:

```
python setup.py install
```

## Quickstart

```
import tsl2591

tsl = tsl2591.Tsl2591()  # initialize
full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
print lux, full, ir
```

## License

Python files in this repository are released under the [MIT license](LICENSE.md).

## FAQ

### Fatal error

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

```
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
