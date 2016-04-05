#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of GrowthRatesPy.
# https://github.com/yoavram/GrowthRatesPy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Yoav Ram <yoav@yoavram.com>
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from .core import *
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
