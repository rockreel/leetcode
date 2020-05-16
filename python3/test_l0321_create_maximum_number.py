import unittest

from l0321_create_maximum_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [9, 8, 6, 5, 3],
            Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
        self.assertEqual(
            [6, 7, 6, 0, 4],
            Solution().maxNumber([6, 7], [6, 0, 4], 5))
        self.assertEqual(
            [9, 8, 9],
            Solution().maxNumber([3, 9], [8, 9], 3))
