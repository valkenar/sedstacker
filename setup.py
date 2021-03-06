#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import sedstacker

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'HISTORY.rst')

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='sedstacker',
    version=sedstacker.__version__,
    license='GNU General Public License v3',
    author='Smithsonian Astrophysical Observatory / Chandra X-Ray Center',
    requires=['astropy'],
    install_requires=['astropy>=0.3, <=0.4.4'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    author_email='jbudynkiewicz@cfa.harvard.edu',
    url='https://github.com/jbudynk/sedstacker',
    description='Astronomical toolkit for statistically combining spectral energy distributions',
    long_description=long_description,
    packages=['sedstacker', 'sedstacker.iris'],
    include_package_data=True,
    platforms='Linux, Mac OSX',
    test_suite='sedstacker.tests',
    classifiers = [
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Astronomers, Developers',
        'License :: OSI Approved :: GNU GPL v3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
