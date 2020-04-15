import unittest

from l0123_best_time_to_buy_and_sell_stock_3 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6,
            Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
        self.assertEqual(
            4,
            Solution().maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(
            0,
            Solution().maxProfit([7, 6, 4, 3, 1]))