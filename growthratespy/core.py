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
from builtins import open
from builtins import str
from future import standard_library
standard_library.install_aliases()
import subprocess
import os
import sys
import functools
import pandas as pd


@functools.lru_cache(maxsize=1)
def find_growthrates():
    try:
        from shutil import which
    except ImportError:
        from distutils.spawn import find_executable
        which = find_executable

    for path in [
        which('GrowthRates'),
        which('GrowthRates.exe'),
        r'C:\Program Files\GrowthRates\GrowthRates.exe',
        r'C:\Program Files (x86)\GrowthRates\GrowthRates.exe',
        r'C:\Program Files\GrowthRates 2.1\GrowthRates.exe',
        r'C:\Program Files (x86)\GrowthRates 2.1\GrowthRates.exe',
        r'C:\Program Files\GrowthRates 2.1 Windows\GrowthRates.exe',
        r'C:\Program Files (x86)\GrowthRates 2.1 Windows\GrowthRates.exe',
        None
    ]:
        if path and os.path.exists(path):
            break
    if not path:
        raise ValueError("Didn't find GrowthRates executable.")
    return path


def growthrates(infile, well=None):
    if not os.path.exists(infile):
        raise ValueError("Path to input file doesn't exist:", infile)
    gr_path = find_growthrates()

    arguments = [gr_path, '-i', infile]
    if well is not None:
        arguments.extend(['-w', str(well)])

    execute_growthrates(arguments)

    base_filename = os.path.splitext(infile)[0]
    # results_filename = base_filename + '.results'
    summary_filename = base_filename + '.summary'
    return read_summary(summary_filename)


def execute_growthrates(arguments):
    status_code = subprocess.call(arguments)
    if status_code != 0:
        raise RuntimeError("GrowthRates returns status code {:d}".format(status_code))


def read_results(results_filename):
    with open(results_filename) as f:
        for line in f:
            if line.startswith('*'):
                break
        return [line.strip() for line in f if line and line != '*' * 57]


def read_summary(summary_filename):
    with open(summary_filename) as f:
        return pd.read_csv(f, sep='\t', skipinitialspace=True, skiprows=1)


if __name__ == '__main__':
    summary = growthrates('../Tecan_210115.tsv', 96, 'D:\\workspace\\GrowthRates 2.1 Windows\\GrowthRates.exe')
    assert summary.shape == (96, 5)
    sys.exit(0)
