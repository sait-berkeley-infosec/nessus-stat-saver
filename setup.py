#!/usr/bin/env python2.7

from setuptools import setup, find_packages

setup(
    name='nessus-stat-saver',
    version='0.0',
    description='Save stats from Nessus',
    author='Arlan Jaska',
    author_email='ajaska@berkeley.edu',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'sqlalchemy',
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
