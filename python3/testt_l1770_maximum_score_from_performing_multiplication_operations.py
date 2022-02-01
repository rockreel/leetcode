import unittest

from l1770_maximum_score_from_performing_multiplication_operations import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            14, 
            Solution().maximumScore([1, 2, 3], [3, 2, 1]))
        self.assertEqual(
            102, 
            Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
