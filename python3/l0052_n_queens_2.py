from typing import List
from typing import Tuple

class Solution:
    def totalNQueens(self, n: int) -> int:

        def can_place(queens: List[Tuple[int, int]], row:int, col:int) -> bool:
            for i, j in queens:
                if i == row or j == col or abs(row - i) == abs(col - j):
                    return False
            return True
        
        def generate_board(queens: List[Tuple[int, int]], n: int) -> List[str]:
            board = [['.'] * n for _ in range(n)]
            for i, j in queens:
                board[i][j] = 'Q'
            return [''.join(r) for r in board]

        def solve(queens: List[Tuple[int, int]], n: int, solution: List[List[Tuple[int, int]]]):
            if len(queens) == n:
                solution.append(generate_board(queens, n))
                return
            
            num_queens = len(queens)
            for j in range(n):
                if can_place(queens, num_queens, j):
                    queens.append((num_queens, j))
                    solve(queens, n, solution)
                    queens.pop()

        solution = []
        queens = []
        solve(queens, n, solution)
        return len(solution)