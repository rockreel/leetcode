import unittest

from l1046_last_stone_weight import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().lastStoneWeight([2,7,4,1,8,1]))
        self.assertEqual(1, Solution().lastStoneWeight([1]))

