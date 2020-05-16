import unittest

from l0319_bulb_switcher import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().bulbSwitch(3))
