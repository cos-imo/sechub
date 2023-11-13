#!/usr/bin/env python

from distutils.core import setup

setup(name='package_name',
      version='1.0',
      description='Your package description here',
      author='Your name',
      author_email='your@email.here',
      url='https://www.python.org/',
      packages=['required_packages'],
      entry_points={
            'console_scripts': [
                'command = main:main',              #replace command
            ],
     },
     )
