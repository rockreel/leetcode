class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        high = 0  # Highest price seen so far from right.
        for p in prices[::-1]:
            high = max(high, p)
            profit = max(profit, high-p)
        return profit

