class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.append(x)
        n = len(self._queue)
        while n > 1:
            self._queue.append(self._queue.pop(0))
            n -= 1
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._queue.pop(0)        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._queue) == 0

