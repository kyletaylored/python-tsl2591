import setuptools

setuptools.setup(
    name='tsl2591',
    version='0.0.3',
    url='http://github.com/maxlklaxl/python-tsl2591',
    author='Max Hofbauer',
    author_email='maxhofb@gmail.com',
    description='Community-coded Python module for TSL2591 sensor. Use at your own risk.',
    license="MIT",
    packages=setuptools.find_packages(),
    long_description=open('README.rst').read(),
    install_requires=['smbus-cffi'],
    py_modules=['tsl2591'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
