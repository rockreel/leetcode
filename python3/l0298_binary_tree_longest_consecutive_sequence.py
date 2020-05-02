"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code her
        def longest_consecutive(root):
            # return (longest end at root, longest of all
            if not root:
                return 0, 0 
            
            left, left_all = longest_consecutive(root.left)
            right, right_all = longest_consecutive(root.right)
            curr = 1
            if left != 0 and root.val + 1 == root.left.val:
                curr = max(curr, 1 + left)
            if right != 0 and root.val + 1 == root.right.val:
                curr = max(curr, 1 + right)
            curr_all = max(curr, max(left_all, right_all))
            return curr, curr_all
        
        return longest_consecutive(root)[1]

