class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # Less prices than trades, just trade on every price up.
        if len(prices) < k:
            max_profit = 0
            for i in range(1, len(prices)):
                max_profit = max_profit + max(prices[i]-prices[i-1], 0)
            return max_profit
        
        # Max profit with at most i trades.
        max_profit = [0] * (k + 1)  
        # Max profit with at most i trades but sold on current day.
        curr_profit = [0] * (k + 1)
        # Find max profit iteratively as seeing more prices.
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(k, 0, -1):  # Iterate j from k to 1 to prevent overwrite max_profit[j-1].
                curr_profit[j] = max(curr_profit[j]+diff, max_profit[j-1]+max(diff, 0))
                max_profit[j] = max(max_profit[j], curr_profit[j])
                
        return max_profit[-1]

