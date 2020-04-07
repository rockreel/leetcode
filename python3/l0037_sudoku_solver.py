from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_candidate(board: List[List[str]], row, col) -> List[str]:
            num_set = set('123456789')
            for j in range(len(board)):
                if board[row][j] != '.' and board[row][j] in num_set:
                    num_set.remove(board[row][j])
            for i in range(len(board)):
                if board[i][col] != '.' and board[i][col] in num_set:
                    num_set.remove(board[i][col])
            board_row = row // 3
            board_col = col // 3
            for i in range(board_row * 3, board_row * 3 + 3):
                for j in range(board_col * 3, board_col * 3 + 3):
                    if board[i][j] != '.' and board[i][j] in num_set:
                        num_set.remove(board[i][j])
            return num_set

        def solve(board: List[List[str]], fill_positions) -> bool:
            if not fill_positions:
                return True
            
            i, j = fill_positions.pop()
            for c in find_candidate(board, i, j):
                board[i][j] = c
                if solve(board, fill_positions):
                    return True

            fill_positions.append((i, j))
            board[i][j] = '.'
            return False
        
        fill_positions = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    fill_positions.append((i, j))
        return solve(board, fill_positions)