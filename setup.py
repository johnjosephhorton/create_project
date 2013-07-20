#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import create_project 

setup(name='create_project',
      version = create_project.__version__,
      author = create_project.__author__ , 
      author_email = create_project.__email__,
      url = 'http://github.com/johnjosephhorton/create_project',
      packages = [''],
      package_data = {'':['*.md', 'templates/*']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['create_project = create_project:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['Jinja2>=2.6'],
      )

