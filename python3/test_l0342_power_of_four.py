import unittest

from l0342_power_of_four import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPowerOfFour(16))
        self.assertEqual(False, Solution().isPowerOfFour(5))