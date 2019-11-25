# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self._stack = [iter(nestedList)]
        self._next_val = self._next()
    
    def _next(self):
        result = None
        while self._stack:
            val = next(self._stack[-1], None)
            if val is None:
                self._stack.pop()
            else:
                if val.isInteger():
                    result = val.getInteger()
                    break
                else:
                    self._stack.append(iter(val.getList()))
        return result

    def next(self):
        """
        :rtype: int
        """
        result = self._next_val
        self._next_val = self._next()
        return result
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next_val is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

