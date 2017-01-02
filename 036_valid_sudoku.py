class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows.
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in num_set:
                    return False
                num_set.add(board[i][j])
        
        # Check columns.
        for i in range(len(board[0])):
            num_set = set()
            for j in range(len(board)): 
                if board[j][i] != '.' and board[j][i] in num_set:
                    return False
                num_set.add(board[j][i])
                
        # Check squares.
        for i in range(3):
            for j in range(3):
                num_set = set()
                for k in range(i*3, i*3+3):
                    for l in range(j*3, j*3+3):
                        if board[k][l] != '.' and board[k][l] in num_set:
                            return False
                        num_set.add(board[k][l])
        
        return True

