class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def num_of_live_neighbours(board, i, j):
            neighbors = [row[max(j-1, 0):j+2] for row in board[max(i-1, 0):i+2]]
            num_live = 0
            for row in neighbors:
                for cell in row:
                    if cell in (1, 3):
                        num_live += 1
            return num_live - board[i][j]
        
        # Mark cell need to be changed: 2: 0 -> 1; 3: 1 -> 0.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if (num_of_live_neighbours(board, i, j) < 2 or
                        num_of_live_neighbours(board, i, j) > 3):
                        board[i][j] = 3
                else:
                    if num_of_live_neighbours(board, i, j) == 3:
                        board[i][j] = 2
        # Update live or dead cell.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
                    

