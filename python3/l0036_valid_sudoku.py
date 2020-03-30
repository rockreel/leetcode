from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in num_set:
                    num_set.add(board[i][j])
                else:
                    return False
        for j in range(len(board)):
            num_set = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in num_set:
                    num_set.add(board[i][j])
                else:
                    return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                # Go through each sub-square.
                num_set = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == '.':
                            continue
                        if board[i+k][j+l] not in num_set:
                            num_set.add(board[i+k][j+l])
                        else:
                            return False

        return True
        