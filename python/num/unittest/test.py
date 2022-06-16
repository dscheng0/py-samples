import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
import datamanip

class TestDataManip(unittest.TestCase):
    def test_flatten_array_basic(self):
        flat_array = datamanip.flatten_array([[1,2,[3]],4])
        self.assertEqual(flat_array, [1,2,3,4])

    def test_flatten_array_raise(self):
        with self.assertRaises(ValueError):
            flat_array = datamanip.flatten_array(['a',"bc",[123]])

if __name__ == '__main__':
    unittest.main()
