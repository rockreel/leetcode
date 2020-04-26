import unittest

from l0241_different_ways_to_add_parentheses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted([0, 2]), sorted(Solution().diffWaysToCompute('2-1-1')))
        self.assertEqual(sorted([-34, -14, -10, -10, 10]), sorted(Solution().diffWaysToCompute('2*3-4*5')))
