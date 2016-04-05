#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of GrowthRatesPy.
# https://github.com/yoavram/GrowthRatesPy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Yoav Ram <yoav@yoavram.com>
from setuptools import setup, find_packages
import versioneer

setup(
    name='GrowthRatesPy',
    version=versioneer.get_version(),
    url='https://growthratespy.yoavram.com',
    license='MIT',
    author='Yoav Ram',
    author_email='yoav@yoavram.com',
    description='Python API to run GrowthRates (Hall et al. 2014)',
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    extras_require={
        'tests': [
            'nose',
            'coverage',
        ]
    },
    include_package_data=True,
    data_files=[
        ('data', [
                'growthratespy/data/Tecan_210115.tsv',
                'growthratespy/data/Tecan_210115.results',
                'growthratespy/data/Tecan_210115.summary'
        ])
    ],
)
