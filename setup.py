#! /usr/bin/env python3
import os
from distutils.core import setup, Extension

if os.name == 'nt':
    ext = Extension(
        'spread',
        ['spreadmodule.c'],
        libraries=['libtspread', 'wsock32'],
        extra_link_args=['/NODEFAULTLIB:libcmt'],
    )
else:
    ext = Extension(
        'spread',
        ['spreadmodule.c'],
        libraries=['tspread-core'],
    )

setup(name='SpreadModule',
      version='1.6',

      maintainer='open-rsx',
      url='https://github.com/open-rsx/spread-python3',

      description='Python 3 bindings for the spread C client API.',

      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python',
          'Topic :: System :: Distributed Computing',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
      ],

      license='Python',
      platforms=['unix', 'ms-windows'],
      ext_modules=[ext])
