# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        nodes = []
        while stack:
            current = stack[-1]
            if current.left or current.right:
                if current.right:
                    stack.append(current.right)
                    current.right = None
                if current.left:
                    stack.append(current.left)
                    current.left = None
            else:
                nodes.append(current.val)
                stack.pop()
        return nodes

