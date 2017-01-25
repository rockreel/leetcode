# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._stack = []
        p = root
        while p and p.left:
            self._stack.append(p)
            p = p.left
        self._current = p

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self._current)
        

    def next(self):
        """
        :rtype: int
        """
        value = self._current.val
        if self._current.right:
            p = self._current.right
            while p.left:
                self._stack.append(p)
                p = p.left
            self._current = p
        else:
            self._current = self._stack.pop() if self._stack else None
        return value
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

