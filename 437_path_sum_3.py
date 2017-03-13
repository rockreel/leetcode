# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSum_(root, sum, prev_sum):
            # All paths start at root and sum to given number.
            if not root:
                return 0
            curr_sum = prev_sum + root.val
            return (1 if curr_sum == sum else 0) + pathSum_(root.left, sum, curr_sum) + pathSum_(root.right, sum, curr_sum)
        
        if not root:
            return 0
        return pathSum_(root, sum, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

