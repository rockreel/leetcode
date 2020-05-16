import unittest

from l0349_intersection_of_two_arrays import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([2], Solution().intersection([1, 2, 2, 1], [2, 2]))
        self.assertEqual([9, 4], Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))