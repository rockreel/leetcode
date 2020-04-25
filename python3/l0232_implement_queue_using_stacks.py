class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack_in = []
        self._stack_out = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack_in.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        return self._stack_out.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        return self._stack_out[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._stack_in) + len(self._stack_out) == 0
          
