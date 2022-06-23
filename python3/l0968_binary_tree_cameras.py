from typing import Optional
from common import TreeNode

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        coverage = set([None])
        self.result = 0
        
        def dfs(node, parent):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            if (parent is None and node not in coverage) or node.left not in coverage or node.right not in coverage:
                self.result += 1
                coverage.update({node, node.left, node.right, parent})

        dfs(root, None)
        return self.result