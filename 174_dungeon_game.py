class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # Required hp at i, j.
        hp = [[0 for _ in row] for row in dungeon]
        hp[-1][-1] = max(-dungeon[-1][-1] + 1, 1)  # Minimum have 1 hp.
        m = len(dungeon)
        n = len(dungeon[0])
        import sys
        for k in range(1, 2*max(m, n)-1):
            i, j = m-1, n-1-k
            while j < n:
                if i >= 0 and j >= 0:
                    next_required_hp = sys.maxint
                    if i < m - 1:
                        next_required_hp = min(hp[i+1][j], next_required_hp)
                    if j < n - 1:
                        next_required_hp = min(hp[i][j+1], next_required_hp)
                    hp[i][j] = max(next_required_hp - dungeon[i][j], 1)
                i -= 1
                j += 1
        return hp[0][0]

