# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        def maxSum(root):
            # Return max path sum from root to leaf and max path sum of tree.
            if not root:
                return -sys.maxint, 0
                
            left_sum, left_sum_leaf = maxSum(root.left)
            right_sum, right_sum_leaf = maxSum(root.right)
            root_sum = root.val + max(left_sum_leaf, 0) + max(right_sum_leaf, 0)
            root_sum_leaf = root.val + max(max(left_sum_leaf, 0), max(right_sum_leaf, 0))
            return (
                max(root_sum, left_sum, right_sum),
                root_sum_leaf,
            )
            
        max_path_sum, _ = maxSum(root)
        return max_path_sum

