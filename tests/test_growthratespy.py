#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of GrowthRatesPy.
# https://github.com/yoavram/GrowthRatesPy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Yoav Ram <yoav@yoavram.com>
from unittest import TestCase
import os
import shutil
import tempfile
import pkg_resources

import pandas as pd

import growthratespy


class Test(TestCase):
    def setUp(self):
        self.filename_tsv = pkg_resources.resource_filename("growthratespy", "data/Tecan_210115.tsv")
        self.filename_results = pkg_resources.resource_filename("growthratespy", "data/Tecan_210115.results")
        self.filename_summary = pkg_resources.resource_filename("growthratespy", "data/Tecan_210115.summary")
        self.folder = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.folder)

    def test_read_summary(self):
        data = growthratespy.read_summary(self.filename_summary)
        self.assertEquals(data.shape, (96, 5))
        self.assertEquals(data.Well.tolist()[-1], 'H12')

    def test_read_results(self):
        data = growthratespy.read_results(self.filename_results)
        self.assertEquals(len([line for line in data if 'Well' in line]), 96)

    def test_growthrates_from_file(self):
        shutil.copy(self.filename_tsv, self.folder)
        just_filename = os.path.split(self.filename_tsv)[-1]
        filename = os.path.join(self.folder, just_filename)
        growthratespy.growthrates(filename, blank_well=96)
        base_filename = os.path.splitext(filename)[0]
        self.assertTrue(os.path.exists(base_filename + '.summary'))
        self.assertTrue(os.path.exists(base_filename + '.results'))

    def test_growthrates_from_data(self):
        data = pd.read_csv(self.filename_tsv, sep='\t')
        ret_val = growthratespy.growthrates(data=data, blank_well=96)
        self.assertIsNotNone(ret_val)

    def test_find_growthrates(self):
        path = growthratespy.find_growthrates()
        self.assertIsNotNone(path)
        self.assertTrue(os.path.exists(path), path)
