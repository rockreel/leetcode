class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_place(queens, i, j):
            for p in queens:
                if p[0] == i or p[1] == j or i - p[0] == j - p[1] or i - p[0] == p[1] - j:
                    return False
            return True
        
        results = 0
        queue = [[]]

        while queue:
            queens = queue.pop(0)
            if len(queens) == n:
                results += 1
                continue
                
            # Place next queen on the next row.
            last_row = queens[-1][0] if queens else -1
            for j in range(n):
                if can_place(queens, last_row+1, j):
                    queue.append(queens + [(last_row+1, j)])
        
        return results

