from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
    
        # Max profit sell a stock at or before ith day.
        max_profit_sell = [0] * len(prices)
        buy_price = prices[0]
        for i in range(1, len(prices)):
            buy_price = min(buy_price, prices[i])
            max_profit_sell[i] = max(max_profit_sell[i-1], prices[i] - buy_price)

        # Max profit buy a stock at or after ith day.
        max_profit_buy = [0] * len(prices)
        sell_price = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            sell_price = max(sell_price, prices[i])
            max_profit_buy[i] = max(max_profit_buy[i+1], sell_price - prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profit_sell[i] + max_profit_buy[i])
        return max_profit