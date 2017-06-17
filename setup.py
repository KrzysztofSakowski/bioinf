#!/usr/bin/env python

from setuptools import setup

setup(name='bioinf',
      version='0.1',
      description='gplmDCA python implementation',
      author='Krzysztof Sakowski, Damian Goworko',
      packages=['functions'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
     )