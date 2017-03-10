# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validateBST(root, min_value, max_value):
            if not root:
                return True
            if root.val >= max_value:
                return False
            if root.val <= min_value:
                return False
            return (
                validateBST(root.left, min_value, root.val) and
                validateBST(root.right, root.val, max_value))
                
        import sys
        return validateBST(root, -sys.maxint, sys.maxint)

