class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def mark_board(board, i, j, visited):
            # Mark connected O cells.
            queue = [(i, j)]
            while queue:
                row, col = queue.pop(0)
                if (row, col) in visited:
                    continue
                board[row][col] = 'R'
                visited.add((row, col))
                if row > 0 and board[row-1][col] == 'O':
                    queue.append((row-1, col))
                if row < len(board)-1 and board[row+1][col] == 'O':
                    queue.append((row+1, col))
                if col > 0 and board[row][col-1] == 'O':
                    queue.append((row, col-1))
                if col < len(board[0])-1 and board[row][col+1] == 'O':
                    queue.append((row, col+1))
        
        if not board or not board[0]:
            return 
        visited = set()
        # Start from O on left and right side.
        for i in range(len(board)):
            if board[i][0] == 'O':
                mark_board(board, i, 0, visited)
            if board[i][len(board[0])-1] == 'O':
                mark_board(board, i, len(board[0])-1, visited)
        # Start from O on top and bottom side.
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                mark_board(board, 0, j, visited)
            if board[len(board)-1][j] == 'O':
                mark_board(board, len(board)-1, j, visited)
        # Remark cells.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

