# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def findPaths(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[str(root.val)]]
            result = []
            result.extend([str(root.val)] + p for p in findPaths(root.left))
            result.extend([str(root.val)] + p for p in findPaths(root.right))
            return result
        paths = findPaths(root)
        return ['->'.join(p) for p in paths]

