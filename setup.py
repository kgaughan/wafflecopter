#!/usr/bin/env python3

import os.path

from setuptools import setup


def read(filename):
    """
    Read files relative to this file.
    """
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with open(full_path, 'r') as fh:
        return fh.read()


setup(
    name='wafflecopter',
    version='0.0.1',
    description='A delicious feed reader!',
    long_description=read('README') + "\n\n" + read('ChangeLog'),
    url='https://github.com/kgaughan/wafflecopter/',
    license='MIT',
    zip_safe=True,

    test_suite='tests.suite',

    install_requires=[
        'docopt',
        'feedparser',
        'Flask',
        'Flask-WTF',
        'peewee',
        'wtforms',
        'wtf-peewee',
    ],

    classifiers=(
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ),

    author='Keith Gaughan',
    author_email='k@stereochro.me',
)
