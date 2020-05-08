class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        # Max profit at day i with stock.    
        stock = [0] * len(prices)
        # Max profit at day i without stock.
        money = [0] * len(prices)
        
        stock[:2] = [-prices[0], max(-prices[0], -prices[1])]
        money[:2] = [0, max(0, prices[1] - prices[0])]
        
        for i in range(2, len(prices)):
            stock[i] = max(stock[i-1], money[i-2] - prices[i])
            money[i] = max(money[i-1], stock[i-1] + prices[i])
        
        return money[-1]
