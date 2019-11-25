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
        while p:
            self._stack.append(p)
            p = p.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        node = self._stack.pop()
        p = node.right
        while p:
            self._stack.append(p)
            p = p.left
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
