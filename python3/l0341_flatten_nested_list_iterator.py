from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:

    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self._value, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self._value


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._stack = [[nestedList, -1]]
        self._next = self._find_next()
    
    def next(self) -> int:
        next_ = self._next
        self._next = self._find_next()
        return next_
    
    def hasNext(self) -> bool:
         return self._next is not None
        
    def _find_next(self):
        while self._stack:
            l, i = self._stack[-1]
            i += 1
            if i >= len(l):
                self._stack.pop()
                continue
            self._stack[-1][1] = i
            if l[i].isInteger():
                return l[i].getInteger()
            else:
                self._stack.append([l[i].getList(), -1])
        return None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
