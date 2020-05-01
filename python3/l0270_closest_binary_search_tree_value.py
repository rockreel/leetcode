from common import TreeNode

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        p = root
        lower = float('-inf')
        upper = float('inf')
        while p:
            if target > p.val:
                lower = max(lower, p.val)
                p = p.right
                
            elif target < p.val:
                upper = min(upper, p.val)
                p = p.left
                
            else:
                return p.val
        if target - lower >= upper - target:
            return upper
        else:
            return lower