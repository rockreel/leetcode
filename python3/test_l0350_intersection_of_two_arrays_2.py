import unittest

from l0350_intersection_of_two_arrays_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted([2, 2]), sorted(Solution().intersect([1, 2, 2, 1], [2, 2])))
        self.assertEqual(sorted([4, 9]), sorted(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])))