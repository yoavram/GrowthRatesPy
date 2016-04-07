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
import tempfile
try:
    from functools import lru_cache
except ImportError:
    from functools32 import lru_cache

import pandas as pd


@lru_cache(maxsize=1)
def find_growthrates():
    """Attempts to find `GrowthRates`.

    Tries to use `shutil.which` or  `distutils.spawn.find_executable`,
    otherwise tries to find it in `Program Files` folder.

    Returns
    -------
    str
        Path to `GrowthRates`; raises `ValueError` if couldn't find.

    """
    try:
        from shutil import which
    except ImportError:
        from distutils.spawn import find_executable as which

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


def growthrates(infile=None, data=None, blank_well=None):
    """Runs `GrowthRates` on input file with blank given well.

    Parameters
    ----------
    infile : str
        path to data file.
    data : pd.DataFrame
        Data to used instead of `infile`.
    blank_well : int
        well number for background OD.

    Returns
    -------
    pandas.DataFrame
        Table of GrowthRates results.
    """
    if not isinstance(blank_well, int) or blank_well <= 0 :
        raise ValueError("blank_well must be a non-negative integer")

    if data is not None:
        infile = tempfile.mktemp(suffix='.tsv')
        data.to_csv(infile, sep='\t', index=False)

    if not os.path.exists(infile):
        raise ValueError("Path to input file doesn't exist:", infile)

    gr_path = find_growthrates()

    arguments = [gr_path, '-i', infile]
    if blank_well is not None:
        arguments.extend(['-w', str(blank_well)])

    _execute_growthrates(arguments)

    base_filename = os.path.splitext(infile)[0]
    # results_filename = base_filename + '.results'
    summary_filename = base_filename + '.summary'
    return read_summary(summary_filename)


def _execute_growthrates(arguments):
    status_code = subprocess.call(arguments)
    if status_code != 0:
        raise RuntimeError("GrowthRates returns status code {:d}".format(status_code))


def read_results(results_filename):
    """Loads a GrowthRates results file.

    Parameters
    ----------
    results_filename : str
        path to results file.

    Returns
    -------
    pandas.DataFrame
        Table of GrowthRates results.
    """
    with open(results_filename) as f:
        for line in f:
            if line.startswith('*'):
                break
        return [line.strip() for line in f if line and line != '*' * 57]


def read_summary(summary_filename):
    """Loads a GrowthRates summary file.

    Parameters
    ----------
    summary_filename : str
        path to summary file.

    Returns
    -------
    pandas.DataFrame
        Table of GrowthRates summary.
    """
    with open(summary_filename) as f:
        return pd.read_csv(f, sep='\t', skipinitialspace=True, skiprows=1)


if __name__ == '__main__':
    summary = growthrates('../Tecan_210115.tsv', 96)
    assert summary.shape == (96, 5)
    sys.exit(0)
