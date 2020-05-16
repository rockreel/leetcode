"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
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


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        def depth_sum(nested_list, depth):
            sum_ = 0
            for n in nested_list:
                if n.isInteger():
                    sum_ += n.getInteger() * depth
                else:
                    sum_ += depth_sum(n.getList(), depth+1)
            return sum_
        return depth_sum(nestedList, 1)

