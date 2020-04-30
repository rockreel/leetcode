from typing import List

class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                if i - 1 >= 0 and board[i-1][j] > 0:
                    live += 1
                if i + 1 < len(board) and board[i+1][j] > 0:
                    live += 1
                if j - 1 >= 0 and board[i][j-1] > 0:
                    live += 1
                if j + 1 < len(board[0]) and board[i][j+1] > 0:
                    live += 1
                if i - 1 >= 0 and j - 1 >= 0 and board[i-1][j-1] > 0:
                    live += 1
                if i + 1 < len(board) and j + 1 < len(board[0]) and board[i+1][j+1] > 0:
                    live += 1
                if i + 1 < len(board) and j - 1 >= 0 and board[i+1][j-1] > 0:
                    live += 1
                if i - 1 >= 0 and j + 1 < len(board[0]) and board[i-1][j+1] > 0:
                    live += 1
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2  # 2 means live -> dead.
                else:
                    if live == 3:
                        board[i][j] = -1 # -1 means dead -> live.
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
