# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, nodes):
            if not root:
                return
            nodes.append(root.val)
            if root.left:
                traverse(root.left, nodes)
            if root.right:
                traverse(root.right, nodes)
        nodes = []
        traverse(root, nodes)
        return nodes

