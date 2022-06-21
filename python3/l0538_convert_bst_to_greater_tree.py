from common import TreeNode
from typing import Optional

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        curr_sum = 0
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                node = stack.pop()
                curr_sum += node.val
                node.val = curr_sum
                if node.left:
                    curr = node.left
        return root