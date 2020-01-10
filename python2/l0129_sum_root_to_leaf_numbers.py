# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def convertListToNum(nums):
            return sum([n*10**i for i, n in enumerate(reversed(nums))])
            
        def getNumbers(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            nums = []
            for n in getNumbers(root.left):
                nums.append([root.val] + n)
            for n in getNumbers(root.right):
                nums.append([root.val] + n)
            return nums
            
        return sum([convertListToNum(n) for n in getNumbers(root)])

