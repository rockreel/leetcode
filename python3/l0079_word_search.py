from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(board, word, row, col, visited):
            if len(word) == 1 and board[row][col] == word:
                return True
            
            if board[row][col] != word[0]:
                return False
            
            visited.add((row, col))
            if row > 0 and (row-1, col) not in visited and search(board, word[1:], row-1, col, visited):
                return True
            if row < len(board) - 1 and (row+1, col) not in visited and search(board, word[1:], row+1, col, visited):
                return True
            if col > 0 and (row, col-1) not in visited and search(board, word[1:], row, col-1, visited):
                return True
            if col < len(board[0]) - 1 and (row, col+1) not in visited and search(board, word[1:], row, col+1, visited):
                return True
            visited.remove((row, col))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, word, i, j, set([])):
                    return True
        return False
    
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