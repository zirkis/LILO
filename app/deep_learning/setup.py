# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import deep_learning

setup(
 
  name='deep_learning',
 
  version='1.0.0',
 
  packages=find_packages(),
 
  author="Benjamin & Kevin",

  description="Deep learning package",

  long_description=open('README.md').read(),
 
  #Enables MANIFEST.in to be taken account
  include_package_data=True,

  classifiers=[
    "Programming Language :: Python",
    "Development Status :: 1 - Planning",
    "License :: MIT",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Topic :: Deep learning",
  ],
 
  setup_requires=['pytest-runner'],

  tests_require=['pytest'],

  license="MIT",
)
