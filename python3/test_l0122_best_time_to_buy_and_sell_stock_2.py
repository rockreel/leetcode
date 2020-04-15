import unittest

from l0122_best_time_to_buy_and_sell_stock_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7,
            Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(
            0,
            Solution().maxProfit([7, 6, 4, 3, 1]))
        self.assertEqual(
            4,
            Solution().maxProfit([1, 2, 3, 4, 5]))