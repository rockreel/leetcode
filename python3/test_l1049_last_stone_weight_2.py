import unittest

from l1049_last_stone_weight_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().lastStoneWeightII([2,7,4,1,8,1]))
        self.assertEqual(5, Solution().lastStoneWeightII([31,26,33,21,40]))
