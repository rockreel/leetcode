import unittest

from l0487_max_consecutive_ones_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            4, 
            Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
        self.assertEqual(
            3, 
            Solution().findMaxConsecutiveOnes([1, 0, 1, 0, 1]
))
        