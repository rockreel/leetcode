class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def existFrom(i, j, board, word):
            # If word exist in board start from i, j.
            if not word:
                return True
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True
                
            tmp = board[i][j]
            board[i][j] = '.'            
            if i - 1 >= 0 and board[i-1][j] != '.' and existFrom(i-1, j, board, word[1:]):
                return True
            if i + 1 < len(board) and board[i+1][j] != '.' and existFrom(i+1, j, board, word[1:]):
                return True
            if j - 1 >= 0 and board[i][j-1] != '.' and existFrom(i, j-1, board, word[1:]):
                return True
            if j + 1 < len(board[0]) and board[i][j+1] != '.' and existFrom(i, j+1, board, word[1:]):
                return True
            board[i][j] = tmp
            return False
        
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                if existFrom(i, j, board, word):
                    return True
        return False

