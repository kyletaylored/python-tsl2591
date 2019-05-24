import setuptools

setuptools.setup(
    name='tsl2591',
    version='0.0.2',
    url='http://github.com/maxlklaxl/tsl2591',
    author='Max Hofbauer',
    author_email='maxhofb@gmail.com',
    description='Community-coded Python module for TSL2591 sensor. Use at your own risk.',
    packages=setuptools.find_packages(),
    long_description=open('README.rst').read(),
    install_requires=['smbus-cffi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
