import unittest

from l0377_combination_sum_4 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(7, Solution().combinationSum4([1,2,3], 4))
        self.assertEqual(0, Solution().combinationSum4([9], 3))
 
