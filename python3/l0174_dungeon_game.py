ass Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    dp[i][j] = max(-dungeon[i][j], 0)
                elif i == len(dungeon) - 1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 0)
                elif j == len(dungeon[0]) - 1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 0)
                else:
                    dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 0)
                
        return dp[0][0] + 1
        
