from typing import List

from l0339_nested_list_weight_sum import NestedInteger

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
