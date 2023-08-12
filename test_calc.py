# our unittest testing.

import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 70)
        self.assertEqual(result, 80)
