from common import TreeNode
from typing import List

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def largest_bst(root: TreeNode, lower: int, upper: int, max_nodes: List[int]) -> int:
            if not root:
                return 0
            if root.val <= lower or root.val >= upper:
                return 0
            
            left_bst = largest_bst(root.left, lower, root.val, max_nodes)
            right_bst = largest_bst(root.right, root.val, upper, max_nodes)

            if ((root.left and left_bst == 0) or
                (root.right and right_bst == 0)):
                return 0

            max_nodes[0] = max(max_nodes[0], 1 + left_bst + right_bst)
            return 1 + left_bst + right_bst
        max_nodes = [0]
        largest_bst(root, float('-inf'), float('inf'), max_nodes)
        return max_nodes[0]

