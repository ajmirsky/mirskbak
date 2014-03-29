#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

dependencies = [

]

links = [
    
]

setup(name='MirskBak',
      version='0.1',
      description='python package for backing up resources',
      author='andrew mirsky',
      author_email='andrew@mirsky.net',
      scripts=[],
      url='https://github.com/ajmirsky/mirskbak.git',
      packages=find_packages(),
      include_package_data=True,
      install_requires=dependencies,
      dependency_links = links,
     )



