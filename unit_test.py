import datetime as dt
import unittest
import logging

import shoppingclass

shop = shoppingclass.VegeSyncer(['collard greens', 'beef steak', 'catfish'], 'sam D')

# MARK: Cliniko Tests
class ClinikoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shop = shop

    @classmethod
    def tearDownClass(cls):
        pass

    def test_getSize_three(self):
        self.assertEqual(self.shop.getSize(), 3)

    def test_getSize(self):
        self.assertNotEqual(self.shop.getSize(), 4)

if __name__ == '__main__':
    unittest.main()
