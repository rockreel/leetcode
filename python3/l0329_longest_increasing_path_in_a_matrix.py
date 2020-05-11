from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def find_longest_path(row: int, col: int, matrix: List[List[int]], longest_paths: List[List[int]]):
            # Calculate longest path starting from (row, col), and record it in longest_paths.
            path_up, path_down, path_left, path_right = 0, 0, 0, 0
            if row - 1 >= 0 and matrix[row][col] < matrix[row-1][col]:
                if longest_paths[row-1][col] != 0:
                    path_up = longest_paths[row-1][col]
                else:
                    path_up = find_longest_path(row-1, col, matrix, longest_paths)
            if row + 1 < len(matrix) and matrix[row][col] < matrix[row+1][col]:
                if longest_paths[row+1][col] != 0:
                    path_down = longest_paths[row+1][col]
                else:
                    path_down = find_longest_path(row+1, col, matrix, longest_paths)
            if col - 1 >= 0 and matrix[row][col] < matrix[row][col-1]:
                if longest_paths[row][col-1] != 0:
                    path_left = longest_paths[row][col-1]
                else:
                    path_left = find_longest_path(row, col-1, matrix, longest_paths)
            if col + 1 < len(matrix[0]) and matrix[row][col] < matrix[row][col+1]:
                if longest_paths[row][col+1] != 0:
                    path_right = longest_paths[row][col+1]
                else:
                    path_right = find_longest_path(row, col+1, matrix, longest_paths)
            longest_paths[row][col] = 1 + max([path_up, path_down, path_left, path_right])
            return longest_paths[row][col]

        longest_paths = [[0 for _ in matrix[0]] for _ in matrix]
        longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if longest_paths[i][j] == 0:
                    find_longest_path(i, j, matrix, longest_paths)
                longest_path = max(longest_path, longest_paths[i][j])
        return longest_path