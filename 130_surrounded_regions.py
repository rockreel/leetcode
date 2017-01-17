class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        # From top to bottom.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or board[i-1][j] == 'R'):
                    board[i][j] = 'R'
            for j in range(len(board[0])-1):               
                if board[i][j] == 'R' and board[i][j+1] == 'O':
                    board[i][j+1] = 'R'
            for j in range(len(board[0])-1, 0, -1):
                if board[i][j] == 'R' and board[i][j-1] == 'O':
                    board[i][j-1] = 'R'
        # From bottom to top    
        for i in range(len(board)-1, -1, -1):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == len(board)-1 or board[i+1][j] == 'R'):
                    board[i][j] = 'R'
            for j in range(len(board[0])-1):
                if board[i][j] == 'R' and board[i][j+1] == 'O':
                    board[i][j+1] = 'R'
            for j in range(len(board[0])-1, 0, -1):
                if board[i][j] == 'R' and board[i][j-1] == 'O':
                    board[i][j-1] = 'R'
        # From left to right.             
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] == 'O' and (j == 0 and board[i][j-1] == 'R'):
                    board[i][j] = 'R'
            for i in range(len(board)-1):
                if board[i][j] == 'R' and board[i+1][j] == 'O':
                    board[i+1][j] = 'R'
            for i in range(len(board)-1, 0, -1):
                if board[i][j] == 'R' and board[i-1][j] == 'O':
                    board[i-1][j] = 'R'
        # From right to left.
        for j in range(len(board[0])-1, -1, -1):
            for i in range(len(board)):
                if board[i][j] == 'O' and (j == len(board[0])-1 and board[i][j+1] == 'R'):
                    board[i][j] = 'R'
            for i in range(len(board)-1):
                if board[i][j] == 'R' and board[i+1][j] == 'O':
                    board[i+1][j] = 'R'
            for i in range(len(board)-1, 0, -1):
                if board[i][j] == 'R' and board[i-1][j] == 'O':
                    board[i-1][j] = 'R'
        # Mark.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

