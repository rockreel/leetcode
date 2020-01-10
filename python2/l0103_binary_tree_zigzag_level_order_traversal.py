# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [None, root]
        left_first = True
        result = []
        while stack[-1] is not None:
            new_stack = [None]
            result.append([])
            while stack[-1] is not None:
                node = stack.pop()
                result[-1].append(node.val)
                if left_first:
                    if node.left:
                        new_stack.append(node.left)
                    if node.right:
                        new_stack.append(node.right)
                else:
                    if node.right:
                        new_stack.append(node.right)
                    if node.left:
                        new_stack.append(node.left)
            left_first = not left_first
            stack = new_stack
        return result

