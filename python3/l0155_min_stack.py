class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []  # Store (value, min of stack)

    def push(self, x: int) -> None:
        min_ = self.getMin()
        if min_ is None:
            self._stack.append((x, x))
        else:
            self._stack.append((x, min(min_, x)))
            
    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
        
    def top(self) -> int:
        return self._stack[-1][0] if self._stack else None

    def getMin(self) -> int:
        return self._stack[-1][1] if self._stack else None
