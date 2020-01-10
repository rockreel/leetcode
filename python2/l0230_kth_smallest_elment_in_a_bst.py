# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(root, k, node):
            # Inorder traverse tree, attach k[0]th node to node.
            # k is a list so it can be modified inside function.
            if not root or node:
                return
            
            traverse(root.left, k, node)
            k[0] -= 1
            if k[0] == 0:
                node.append(root.val)
            traverse(root.right, k, node)
        
        node, k = [], [k]
        traverse(root, k, node)
        return node[0]

