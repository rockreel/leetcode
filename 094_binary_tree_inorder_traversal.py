# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        nodes = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                nodes.append(node.val)
                if node.right:
                    current = node.right
        return nodes

# Recursive.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_traverse(root, nodes):
            if not root:
                return
            inorder_traverse(root.left, nodes)
            nodes.append(root.val)
            inorder_traverse(root.right, nodes)
            return
        
        nodes = []
        inorder_traverse(root, nodes)
        return nodes
