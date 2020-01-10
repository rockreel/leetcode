class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_values = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if not self._min_values or self._min_values[-1] >= x:
            self._min_values.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        x = self._stack.pop()
        if x == self._min_values[-1]:
            self._min_values.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_values[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

