#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Auto Pontomais",
    version="0.1",
    author="Gabryel Monteiro",
    author_email="gabryelARM@gmail.com",
    description=("Simple Pontomais script."),
    license="MIT",
    url="http://github.com/Megamiun/auto_pontomais",
    install_requires=read('requirements.txt'),
    packages=['auto_pontomais'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3'
    ],
    scripts="auto_pontomais"
)
