import unittest

from l0265_paint_house_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(10, Solution().minCostII([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
        self.assertEqual(5, Solution().minCostII([[5]]))