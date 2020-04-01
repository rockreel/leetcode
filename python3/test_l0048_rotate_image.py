import unittest

from l0048_rotate_image import Solution

class Test(unittest.TestCase):

    def test_solution(self):
        m1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        m1r = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        Solution().rotate(m1)
        self.assertEqual(m1r, m1)
        m2 = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        m2r = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        Solution().rotate(m2)
        self.assertEqual(m2r, m2)