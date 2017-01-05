class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def can_place(queens, i, j):
            for p in queens:
                if p[0] == i or p[1] == j or i - p[0] == j - p[1] or i - p[0] == p[1] - j:
                    return False
            return True
        
        results = []
        queue = [[]]

        while queue:
            queens = queue.pop(0)
            if len(queens) == n:
                results.append(queens)
                continue
                
            # Place next queen on the next row.
            last_row = queens[-1][0] if queens else -1
            for j in range(n):
                if can_place(queens, last_row+1, j):
                    queue.append(queens + [(last_row+1, j)])
        
        boards = []
        for result in results:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for r in result:
                board[r[0]][r[1]] = 'Q'
            boards.append([''.join(b) for b in board])
                
        return boards

