import unittest

from l0322_coin_change import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().coinChange([1, 2, 5], 11))
        self.assertEqual(-1, Solution().coinChange([2], 3))
