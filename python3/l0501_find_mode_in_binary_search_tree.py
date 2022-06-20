from common import TreeNode
from typing import Optional, List

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        max_freq = 0
        curr_freq = 0
        max_values = []
        pre = None
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if not pre:
                    curr_freq = 1
                elif node.val != pre.val:
                    curr_freq = 1
                else:
                    curr_freq += 1

                if curr_freq > max_freq:
                    max_freq = curr_freq
                    max_values = [node.val]
                elif curr_freq == max_freq:
                    max_values.append(node.val)

                pre = node 
                if node.right:
                    curr = node.right
                    
        return max_values