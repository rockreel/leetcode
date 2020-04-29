import unittest

from l0283_move_zeros import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = [0, 1, 0, 3, 12]
        Solution().moveZeroes(l)
        self.assertEqual([1, 3, 12, 0, 0], l)
