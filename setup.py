# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="pyapdl",
    version='0.1.0.dev0',
    description='Programming in ANSYS Parametric Design Language using Python',
    author='Pedro Jorge De Los Santos',
    author_email='delossantosmfq@gmail.com',
    license = "MIT",
    keywords=["FEA","ANSYS","APDL"],
    install_requires=["numpy"],
    url='https://github.com/JorgeDeLosSantos/pyapdl',
    packages=['pyapdl'],
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "Intended Audience :: Science/Research",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: Implementation :: CPython",
      "Topic :: Scientific/Engineering",
      "Topic :: Utilities",
    ],
)
