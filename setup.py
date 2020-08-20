#!/usr/bin/env python
from setuptools import setup    
setup(name='qdill',
      version='1.0',
      description='tiny convenience lib for dill',
      author='madgen',
      author_email='madgencontent@gmail.com',
      url='https://github.com/madgen-content/qdill',
      install_requires=['dill'],
      packages=['qdill']
     )