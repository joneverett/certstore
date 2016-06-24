#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'certstore'
copyright = '2016, Jon Everett'
author = 'Jon Everett'

# The short X.Y version.
version = '0.0.2'
# The full version, including alpha/beta/rc tags.
release = '0.0.2'
