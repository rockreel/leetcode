# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # Count left and right most depths.
        l, r = 1, 1
        p = root
        while p.left:
            p = p.left
            l += 1
        p = root
        while p.right:
            p = p.right
            r += 1
        
        if l == r:
            # Perfect tree.
            return 2**l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

