class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs:
            return 0
        dp = [[0] * len(costs[0]) for _ in range(len(costs)+1)]
        min_idx = [0, 0]
        for i in range(1, len(costs)+1):
            new_min_idx = []
            for j in range(len(costs[0])):
                if j != min_idx[0]:
                    dp[i][j] = dp[i-1][min_idx[0]] + costs[i-1][j]
                else:
                    dp[i][j] = dp[i-1][min_idx[1]] + costs[i-1][j]
                if not new_min_idx:
                    new_min_idx.append(j)
                elif dp[i][j] < dp[i][new_min_idx[0]]:
                    new_min_idx.insert(0, j)
                elif len(new_min_idx) == 1 or dp[i][j] < dp[i][new_min_idx[1]]:
                    new_min_idx.insert(1, j)
            min_idx = new_min_idx
        return min(dp[-1])
