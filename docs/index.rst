.. GrowthRatesPy documentation master file, created by
   sphinx-quickstart on Wed Mar 30 21:21:47 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=========================================
GrowthRatesPy: Python API for GrotwhRates
=========================================

**Author**: `Yoav Ram <http://www.yoavram.com>`_

`GrowthRates <https://sourceforge.net/projects/growthrates/>`_ is a program for analysis of growth curve data:
"GrowthRates uses the output from microbial growth rate experiments that are done using microtiter plate readers
to caculate the best-fit growth rates, the lag times and the maximum OD".

**GrowthRatesPy** provides a Python API for using **GrowthRates** from within Python code.

Install
-------

To install the latest stable version of **GrowthRatesPy**, use `pip`:

>>> pip install git+https://github.com/yoavram/GrowthRatesPy.git

You will need to install `pandas <http://pandas.pydata.org/>`_, which requires NumPy etc.
This is most easily done on Windows using `Anaconda <https://store.continuum.io/>`_ .

You will also need to download `GrowthRates <https://sourceforge.net/projects/growthrates/>`_
and unzip it to either `C:\\Program Files`, `C:\\Program Files (x86)` or to anywhere else of your choice,
provided that you add it to your `PATH`.

**GrowthRatesPy** supports both Python 2 and 3 and was tested with Python 2.7 and 3.4.

Usage
-----

To use **GrowthRatesPy** you'll need a TSV (tab-separated values) file in the format specified in **GrowthRates** documentation:
one time column, in minutes, called `Min`, and one or more columns of OD data (usually one column per well).

You can use the file supplied with the package, called `Tecan_210115.tsv`,
which will be located in your Python package library (search is your friend).

>>> from growthratespy import growthrates
>>> summary = growthrates(infile='Tecan_210115.tsv', well=96)

Here, `well` is the number of the well that has the blank sample.

The result, `summary`, is a table of type `pandas.DataFrame` that contains the results of the analysis:

.. csv-table::
  :file: _static/Tecan_210115.summary.head8.csv

If the data is in a `pandas.DataFrame` called `df` rather than a file,
you can give this dataframe directly to the `growthrates` function:

>>> summary = growthrates(data=df, well=96)

Support
-------

Please report bugs and file feature requests by `opening an issue on github <https://github.com/yoavram/GrowthRatesPy/issues>`_.

Citation
--------
If you use **GrowthRates**, please cite:

.. note::

   Hall, B. G., H. Acar and M. Barlow. 2014 *Growth Rates Made Easy*. Mol. Biol. Evol. 31:
   232-238 doi:10.1093/molbev/mst197

License
-------

**GrowthRatesPy** is not related to **GrowthRates** and is independently developed.

**GrowthRatesPy** source code is licensed under the terms of the `MIT license <http://opensource.org/licenses/MIT>`_.

**GrowthRatesPy** documentation and other content is licensed under the terms of the `Attribution 4.0 International (CC BY 4.0) license <https://creativecommons.org/licenses/by/4.0/>`_.

**GrowthRates** is distributed under a separate license, please see the PDF attached to the program.

API
---

.. automodule:: growthratespy.core
    :members:

