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

    def totalNQueens2(self, n: int) -> int:
        def canAttack(q1, q2):
            if q1[0] == q2[0]:
                return True
            if q1[1] == q2[1]:
                return True
            if abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]):
                return True
            return False
        
        def placeQueen(queens, row, n, result):
            if len(queens) == n:
                result.append(queens)
                return
            
            for i in range(n):
                can_attack = False
                for q in queens:
                    if canAttack(q, (row, i)):
                        can_attack = True
                        break
                if not can_attack:
                    queens.append((row, i))
                    placeQueen(queens, row + 1, n, result)
                    queens.pop()
            return 
        
        result = []
        placeQueen([], 0, n, result)
        return len(result)