# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def rob(root):
            # Return max money by robbing root and  not robbing root.
            if not root:
                return 0, 0
            rob_left, not_rob_left = rob(root.left)
            rob_right, not_rob_right = rob(root.right)
            rob_root = root.val + not_rob_left + not_rob_right
            not_rob_root = rob_left + rob_right
            return max(rob_root, not_rob_root), rob_left+rob_right
            
        return rob(root)[0]

