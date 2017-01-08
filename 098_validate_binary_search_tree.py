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
                
            if max_value is not None and root.val >= max_value:
                return False
            if min_value is not None and root.val <= min_value:
                return False
            
            return (
                validateBST(root.left, min_value, root.val) and
                validateBST(root.right, root.val, max_value))
        
        return validateBST(root, None, None)

