import unittest

from l0485_max_consecutive_ones import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3, 
            Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
        self.assertEqual(
            2, 
            Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
        