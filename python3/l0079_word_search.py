from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def exist_at(board: List[List[str]], word: str, row: int, col: int) -> bool:
            if not word:
                return True
            if row - 1 >= 0 and board[row-1][col] == word[0]:
                board[row-1][col] = ''
                if exist_at(board, word[1:], row-1, col):
                    return True
                board[row-1][col] = word[0]
            if row + 1 < len(board) and board[row+1][col] == word[0]:
                board[row+1][col] = ''
                if exist_at(board, word[1:], row+1, col):
                    return True
                board[row+1][col] = word[0]
            if col - 1 >= 0 and board[row][col-1] == word[0]:
                board[row][col-1] = ''
                if exist_at(board, word[1:], row, col-1):
                    return True
                board[row][col-1] = word[0]
            if col + 1 < len(board[0]) and board[row][col+1] == word[0]:
                board[row][col+1] = ''
                if exist_at(board, word[1:], row, col+1):
                    return True
                board[row][col+1] = word[0]
            return False
        
        if not word:
            return True
        if not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    if exist_at(board, word[1:], i, j):
                        return True
                    board[i][j] = word[0]
        return False