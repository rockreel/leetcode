class TicTacToe:

    def __init__(self, n: int):
        self._row = [[0] * n, [0] * n]
        self._col = [[0] * n, [0] * n]
        self._diag = [0, 0]
        self._rdiag = [0, 0]
        self._n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        @return The current winning condition, can be either
          0: No one wins.
          1: Player 1 wins.
          2: Player 2 wins.
        """
        self._row[player-1][row] += 1
        self._col[player-1][col] += 1
        if row == col:
            self._diag[player-1] += 1
        if row == self._n - col:
            self._rdiag[player-1] += 1
        if (self._row[player-1][row] == self._n or
            self._col[player-1][col] == self._n or
            self._diag[player-1] == self._n or
            self._rdiag[player-1] == self._n):
            return player
        return 0