import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
import datamanip
import temptracker

class TestDataManip(unittest.TestCase):
    def test_flatten_array_basic(self):
        """
        Test basic functionality of flatten_array
        """
        flat_array = datamanip.flatten_array([[1,2,[3]],4])
        self.assertEqual(flat_array, [1,2,3,4])

    def test_flatten_array_raise(self):
        """
        Test error conditions of flatten_array
        """
        with self.assertRaises(ValueError):
            flat_array = datamanip.flatten_array(['a',"bc",[123]])

class TestTempTracker(unittest.TestCase):
    def test_temp_tracker_init(self):
        """
        Test initial state of TempTracker
        """
        tracker = temptracker.TempTracker()
        with self.assertRaises(RuntimeWarning):
            tracker.get_min()
        with self.assertRaises(RuntimeWarning):
            tracker.get_max()
        with self.assertRaises(RuntimeWarning):
            tracker.get_mean()

    def test_temp_tracker_basic(self):
        """
        Test basic functionality of TempTracker
        """
        tracker = temptracker.TempTracker()
        temps = range(0, 111, 10)
        for temp in temps:
            tracker.insert(temp)
        self.assertEquals(tracker.get_min(), min(temps))
        self.assertEquals(tracker.get_max(), max(temps))
        self.assertEquals(tracker.get_mean(), float(sum(temps))/len(temps))

if __name__ == '__main__':
    unittest.main()
