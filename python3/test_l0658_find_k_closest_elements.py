import unittest

from l0658_find_k_closest_elements import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 2, 3, 4], Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
        self.assertEqual([1, 2, 3, 4], Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1))
