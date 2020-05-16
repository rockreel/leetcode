import unittest

from l0326_power_of_three import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPowerOfThree(27))
        self.assertEqual(False, Solution().isPowerOfThree(0))
        self.assertEqual(True, Solution().isPowerOfThree(9))
        self.assertEqual(False, Solution().isPowerOfThree(45))
