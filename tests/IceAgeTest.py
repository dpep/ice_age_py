#!/usr/bin/env python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from ice_age import IceAge, TestCase

os.environ['ICE_AGE_TEST'] = '123'


# class IceAgeTest(unittest.TestCase):
class IceAgeTest(TestCase):
    def checkEnv(self, modified=False):
        fn = self.assertNotEqual if modified else self.assertEqual
        fn(
            '123',
            os.environ['ICE_AGE_TEST']
        )

    def test_setup(self):
        self.checkEnv()
        self.assertTrue(IceAge.isFrozen())


    def test_basic(self):
        os.environ['ICE_AGE_TEST'] = 'xxx'
        self.checkEnv(True)

    def test_reset(self):
        self.checkEnv()



if __name__ == '__main__':
    unittest.main()
