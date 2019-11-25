# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flattree(root):
            # Return tail node of the flatten tree.
            if not root.left and not root.right:
                return root
            
            left_root = root.left
            right_root = root.right
            tail = root
            
            if left_root:
                left_tail = flattree(left_root)
                tail.right = left_root
                tail.left = None
                tail = left_tail

            if right_root:
                right_tail = flattree(right_root)
                tail.right = right_root
                tail.left = None
                tail = right_tail

            return tail
        
        if not root:
            return root
        flattree(root)

