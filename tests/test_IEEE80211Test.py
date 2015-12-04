#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_IEEE80211Test
----------------------------------

Tests for `IEEE80211Test` module.
"""

import unittest

from IEEE80211Test import IEEE80211Test


class TestIeee80211test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_fib(self):
        assert(55 == IEEE80211Test.fib(10))
        assert(1 == IEEE80211Test.fib(1))

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
