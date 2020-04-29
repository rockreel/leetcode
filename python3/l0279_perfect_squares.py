import math

class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] num perfect squares for i.
        dp = list(range(n+1))
        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]

    def numSquaresBFS(self, n: int) -> int:
        queue = [(n, 0)]
        while queue:
            target, level = queue.pop(0)
            if target == 0:
                return level
            for i in range(int(math.sqrt(target)), 0, -1):
                queue.append((target - i**2, level + 1))
            