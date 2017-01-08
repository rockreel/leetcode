# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateBST(nums):
            if not nums:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            trees = []
            for i, num in enumerate(nums):
                for t1 in generateBST(nums[:i]):
                    for t2 in generateBST(nums[i+1:]):
                        root = TreeNode(num)
                        root.left = t1
                        root.right = t2
                        trees.append(root)
            return trees
        
        if n == 0:
            return []
        nums = range(1, n+1)
        return generateBST(nums)

