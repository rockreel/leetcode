from typing import List
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def min_cost(i):
            if i >= len(days):
                return 0
            result = float('inf')
            result = min(result, costs[0] + min_cost(i+1))
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            result = min(result, costs[1] + min_cost(j))
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            result = min(result, costs[2] + min_cost(j))
            
            return result
        
        return min_cost(0)