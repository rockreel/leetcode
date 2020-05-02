import unittest

from l0256_paint_house import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(10, Solution().minCost([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))
