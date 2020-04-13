class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = dp[i] + dp[j] * dp[i-j-1]
        return dp[-1]

    def numTreesRecursive(self, n: int) -> int:
        if n <= 1:
            return 1
        num_trees = 0
        for i in range(n):
            num_trees += self.numTrees(i) * self.numTrees(n-i-1)
        return num_trees