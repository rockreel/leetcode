# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findLeftLeaves(root, prev_root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                if prev_root and prev_root.left == root:
                    leaves.append(root.val)
                return
            findLeftLeaves(root.left, root, leaves)
            findLeftLeaves(root.right, root, leaves)
            
        leaves = []
        findLeftLeaves(root, None, leaves)
        return sum(leaves)

