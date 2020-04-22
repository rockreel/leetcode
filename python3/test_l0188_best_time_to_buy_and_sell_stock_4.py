import unittest

from l0188_best_time_to_buy_and_sell_stock_4 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().maxProfit(2, [2, 4, 1]))
        self.assertEqual(7, Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))