from common import TreeNode
from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        curr = root
        stack = []
        pre = None
        min_abs = float('inf')
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if pre:
                    min_abs = min(min_abs, node.val - pre.val)
                pre = node
                if node.right:
                    curr = node.right
        return min_abs