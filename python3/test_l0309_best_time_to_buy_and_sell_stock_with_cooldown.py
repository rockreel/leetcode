import unittest

from l0309_best_time_to_buy_and_sell_stock_with_cooldown import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().maxProfit([1, 2, 3, 0, 2]))
