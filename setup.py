#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name='IEEE80211Test',
    version='0.1.0',
    description="Test 802.11 performance using Python",
    long_description=readme + '\n\n' + history,
    author="Ydfang",
    author_email='ydfang@hotmail.com',
    url='https://github.com/ydfang/IEEE80211Test',
    packages=[
        'IEEE80211Test',
    ],
    package_dir={'IEEE80211Test':
                 'tests'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='IEEE80211Test',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests.test_IEEE80211Test',
    tests_require=test_requirements,
)
