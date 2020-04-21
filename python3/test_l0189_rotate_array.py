import unittest

from l0189_rotate_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(l, 3)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], l)

        l = [-1, -100, 3, 99]
        Solution().rotate(l, 2)
        self.assertEqual([3, 99, -1, -100], l)