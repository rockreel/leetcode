from common import TreeNode
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        paths = []
        for p in self.pathSum(root.left, sum - root.val):
            paths.append([root.val] + p)

        for p in self.pathSum(root.right, sum - root.val):
            paths.append([root.val] + p)

        return paths
        