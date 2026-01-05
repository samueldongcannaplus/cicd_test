import unittest
import shoppingclass

shop = shoppingclass.VegeSyncer()

class VegeTestCase(unittest.TestCase):
    def test_test_valid(self):
        self.assertEqual(shop.test(), 1)
    
    def test_test_invalid(self):
        self.assertEqual(shop.test(), 2)