class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        # The maximum profit if buy a stock at or after i.
        buy_after = [0] * len(prices)
        prev_max_profit = 0
        prev_highest = 0
        for i in range(len(prices)-1, -1, -1):
            highest = max(prev_highest, prices[i])
            profit = max(highest-prices[i], 0)
            buy_after[i] = max(profit, prev_max_profit)
            prev_max_profit = buy_after[i]
            prev_highest = highest
        
        # The maximum profit if sell a stock at or before i.
        sell_before = [0] * len(prices)
        prev_max_profit = 0
        prev_lowest = prices[0]
        for i in range(len(prices)):
            lowest = min(prev_lowest, prices[i])
            profit = max(prices[i]-lowest, 0)
            sell_before[i] = max(profit, prev_max_profit)
            prev_max_profit = sell_before[i]
            prev_lowest = lowest

        profit = 0
        for i in range(len(prices)):
            profit = max(profit, sell_before[i]+buy_after[i])
            
        return profit

