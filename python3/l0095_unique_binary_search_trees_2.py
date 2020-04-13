from common import TreeNode
from typing import List

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate_trees(nums: List[int]) -> List[TreeNode]:
            if not nums:
                return [None]

            trees = []
            for i, n in enumerate(nums):
                for left_tree in generate_trees(nums[:i]):
                    for right_tree in generate_trees(nums[i+1:]):
                        root = TreeNode(n)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees
        
        if n == 0:
            return []
        nums = [i for i in range(1, n+1)]
        return generate_trees(nums)