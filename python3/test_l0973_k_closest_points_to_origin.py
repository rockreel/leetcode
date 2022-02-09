import unittest

from l0973_k_closest_points_to_origin import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[-2,2]]), 
            sorted(Solution().kClosest([[1,3],[-2,2]], 1)))
        self.assertEqual(
            sorted([[3,3],[-2,4]]), 
            sorted(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)))
