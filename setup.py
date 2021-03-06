#!/usr/bin/env python3
from setuptools import setup, find_packages
from glob import glob
setup(name='data_stores',
    version='1.0.0',
    description='Code generator for modbus libraries',
    url='',
    author='ElectroOptical Innovations, LLC.',
    author_email='simon.hobbs@electrooptical.net',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'jinja2',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=list(glob("bin/*")),
    include_package_data=True,
    zip_safe=True
)
