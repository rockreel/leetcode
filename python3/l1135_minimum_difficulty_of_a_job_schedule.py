from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][j]: min job difficulty for i + 1 day and first j + 1 jobs
        dp = [[-1] * len(jobDifficulty) for _ in range(d)]
        difficulty = -1
        for j in range(len(jobDifficulty)):
            difficulty = max(jobDifficulty[j], difficulty)
            dp[0][j] = difficulty

        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                difficulty = -1
                min_difficulty = float('inf')
                for k in range(j, i-1, -1):
                    difficulty = max(jobDifficulty[k], difficulty)
                    min_difficulty = min(min_difficulty, dp[i-1][k-1] + difficulty)
                dp[i][j] = min_difficulty

        return dp[-1][-1]