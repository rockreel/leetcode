class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = []
        self._stack_backup = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self._stack:
            self._stack_backup.append(self._stack.pop())
        self._stack.append(x)
        while self._stack_backup:
            self._stack.append(self._stack_backup.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self._stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

