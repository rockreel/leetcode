# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def inorderTraverse(root, nodes):
            if not root:
                return
            inorderTraverse(root.left, nodes)
            nodes.append(root.val)
            inorderTraverse(root.right, nodes)
            
        nodes = []
        inorderTraverse(root, nodes)
        return nodes

