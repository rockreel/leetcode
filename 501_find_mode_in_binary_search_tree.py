# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, counter):
            if not root:
                return
            counter[root.val] += 1
            traverse(root.left, counter)
            traverse(root.right, counter)
            
        from collections import defaultdict
        counter = defaultdict(int)
        traverse(root, counter)
        max_count = max(counter.values()) if counter else 0
        return [v for v, c in counter.iteritems() if c == max_count]

