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

    def solveSudokuBoardIteration(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, c, board):
            for i in range(9):
                if board[i][col] == c:
                    return False
            for j in range(9):
                if board[row][j] == c:
                    return False
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] == c:
                        return False
            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    for c in '123456789':
                        if not is_valid(i, j, c, board):
                            continue
                        board[i][j] = c
                        if solve(board):
                            return True
                        board[i][j] = '.'
                    return False
            return True
        
        solve(board)
        return