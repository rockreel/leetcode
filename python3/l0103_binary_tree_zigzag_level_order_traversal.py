from common import TreeNode
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        levels = []
        left_to_right = True
        while stack:
            stack_next = []
            levels.append([])
            while stack:
                node = stack.pop()
                levels[-1].append(node.val)
                if left_to_right:
                    if node.left:
                        stack_next.append(node.left)
                    if node.right:
                        stack_next.append(node.right) 
                else:
                    if node.right:
                        stack_next.append(node.right)
                    if node.left:
                        stack_next.append(node.left)
            left_to_right = not left_to_right
            stack = stack_next

        return levels