from common import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self._stack = []
        self._current = root
        self._next = self._getNext()
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        next = self._next
        self._next = self._getNext()
        return next
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._next is not None
        
    def _getNext(self) -> TreeNode:
        while self._current or self._stack:
            if self._current:
                self._stack.append(self._current)
                self._current = self._current.left
            else:
                node = self._stack.pop()
                if node.right:
                    self._current = node.right
                return node.val
                


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
