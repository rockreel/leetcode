from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def max_profit(fee, i, hold):
            if i >= len(prices):
                return 0

            if hold:
                return max(prices[i] - fee + max_profit(fee, i + 1, False), max_profit(fee, i + 1, True))
            else:
                return max(-prices[i] + max_profit(fee, i + 1, True), max_profit(fee, i + 1, False))

        return max_profit(fee, 0, False)