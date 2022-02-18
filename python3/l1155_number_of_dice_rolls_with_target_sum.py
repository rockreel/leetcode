from typing import List
from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def num_rolls(n, k, target):
            if target < 1:
                return 0
            if n == 1:
                if 1 <= target <= k:
                    return 1
                else:
                    return 0
            result = 0
            for i in range(1, k+1):
                result += num_rolls(n-1, k, target-i)
            return result
        return num_rolls(n, k, target) % (10**9 + 7)