from common import TreeNode
from typing import List

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def root_to_leaf_numbers(root: TreeNode) -> List[List[int]]:
            if not root.left and not root.right:
                return [[root.val]]
            numbers = []
            if root.left:
                for n in root_to_leaf_numbers(root.left):
                    numbers.append([root.val] + n)
            if root.right:
                for n in root_to_leaf_numbers(root.right):
                    numbers.append([root.val] + n)
            return numbers
        if not root:
            return 0
        numbers = root_to_leaf_numbers(root)
        result = 0
        for number in numbers:
            for i, n in enumerate(reversed(number)):
                result += (10 ** i) * n
        return result