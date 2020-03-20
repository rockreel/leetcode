import unittest

from l0016_3_sum_closest import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().threeSumClosest([-1,2,1,-4], 1))