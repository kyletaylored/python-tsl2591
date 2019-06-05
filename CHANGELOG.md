<a name="0.1.5"></a>
## [0.1.5] - 2019-06-05
- [Updating name, adding package scaffolding from CookieCutter](https://github.com/audreyr/cookiecutter-pypackage)
- Added Travis CI config (removed a test because it only works on Raspbian or devices with I2C enabled)
- Updated scaffold from existing files
- Updating package name for consistency (python_tsl2591)
- Published to [PyPi](https://pypi.org/project/python-tsl2591/)

<a name="0.1.4"></a>
## [0.1.4] - 2019-06-04
- Added CHANGELOG
- Published to [PyPi](https://pypi.org/project/tsl2591/)

<a name="0.1.3"></a>
## [0.1.3] - 2019-06-04
- Added packaging files for PyPi
- Added Manifest, updated README
- Updated setup.py based on https://github.com/kennethreitz/setup.py (modernized)
- Replace smbus/smbus-cffi with smbus2, a Python-only derivative. Removes the requirement to have smbus package installed on system.
- Linted for PEP8
- Updated class name for clarity, clean up variables
- Added instructions for installation
- Added common get_current() function with JSON response option
- Fixes integration_time plus **1** second blocked reliable measures (issue #10)

<a name="0.0.1"></a>
## [0.0.1] - 2016-03-06
- [Changed order of reading the registers in get_full_luminosity(self)](https://github.com/maxlklaxl/python-tsl2591/pull/6)
- [Fix get_luminostiy function and self test code](https://github.com/maxlklaxl/python-tsl2591/pull/4)
- [Corrects an error in the get_gain code](https://github.com/maxlklaxl/python-tsl2591/pull/3)

<a name="0.0.0"></a>
## 0.0.0 - 2015-05-07
- Initial release

[0.1.4]: https://github.com/maxlklaxl/python-tsl2591/compare/0.0.1...0.1.4
[0.1.3]: https://github.com/maxlklaxl/python-tsl2591/compare/0.0.1...0.1.3
[0.0.1]: https://github.com/maxlklaxl/python-tsl2591/compare/0.0.0...0.0.1
