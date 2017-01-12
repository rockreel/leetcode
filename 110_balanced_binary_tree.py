# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBalancedTree(root):
            # Return (depth, if balanced)
            if not root:
                return (0, True)
            left_depth, left_is_balanced = isBalancedTree(root.left)
            right_depth, right_is_balanced = isBalancedTree(root.right)
            is_balanced = (left_is_balanced and
                           right_is_balanced and
                           abs(left_depth-right_depth) <= 1)
            return (max(left_depth, right_depth)+1, is_balanced)
            
        
        return isBalancedTree(root)[1]

