class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solve_one(board, i, j):
            # Return candidate numbers at i, j.
            num_set = set('123456789')
            for k in range(len(board)):
                if board[i][k] != '.' and board[i][k] in num_set:
                    num_set.remove(board[i][k])       
            for k in range(len(board)):
                if board[k][j] != '.' and board[k][j] in num_set:
                    num_set.remove(board[k][j])
            for k in range((i/3)*3, (i/3)*3 + 3):
                for l in range((j/3)*3, (j/3)*3 + 3):
                    if board[k][l] != '.' and board[k][l] in num_set:
                        num_set.remove(board[k][l])
            return num_set
            
        def solve(board, positions_to_fill):
            # If solved, return True and modify board in place,
            # otherwise return False and not modify board.
            if not positions_to_fill:
                return True
            
            i, j = positions_to_fill.pop()
            for c in solve_one(board, i, j):
                board[i][j] = c
                if solve(board, positions_to_fill):
                    return True
            
            # Change board back.
            positions_to_fill.append((i, j))
            board[i][j] = '.'
            return False
        
        positions_to_fill = []
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] == '.':
                    positions_to_fill.append((i, j))
        solve(board, positions_to_fill)  

