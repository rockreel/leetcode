from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def fill_board(board: List[List[str]], row: int, col: int) -> None:
            board[row][col] = '.'
            if row - 1 >= 0 and board[row-1][col] == 'O':
                fill_board(board, row-1, col)
            if row + 1 < len(board) and board[row+1][col] == 'O':
                fill_board(board, row+1, col)
            if col - 1 >= 0 and board[row][col-1] == 'O':
                fill_board(board, row, col-1)
            if col + 1 < len(board[0]) and board[row][col+1] == 'O':
                fill_board(board, row, col+1)

        if not board or not board[0]:
            return
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                fill_board(board, i, 0)
            if board[i][len(board[0])-1] == 'O':
                fill_board(board, i, len(board[0])-1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                fill_board(board, 0, j)
            if board[len(board)-1][j] == 'O':
                fill_board(board, len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return

