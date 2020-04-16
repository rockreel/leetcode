from common import TreeNode
from typing import List

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def max_sum_path(root: TreeNode, max_sum: List[int]) -> int:
            # max_sum is to record the max sum of any path goes through root.
            if not root:
                return 0
            max_sum_left = max_sum_path(root.left, max_sum)
            max_sum_right = max_sum_path(root.right, max_sum)
            # If max_sum_left or max_sum_right, then do not include that path.
            max_sum[0] = max(
                max_sum[0],
                root.val + max(max_sum_left, 0) + max(max_sum_right, 0))
            # If both max_sum_left and max_sum_right are negative, then do not include those paths.
            return root.val + max(max(max_sum_left, max_sum_right), 0)

        max_sum = [float('-inf')]
        max_sum_root = max_sum_path(root, max_sum)
        return max_sum[0]

