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

# No extra space solution, in order traverse and counting.
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(curr_node, last_node, curr_count, max_count, modes):
            # Return the last node traversed.
            if not curr_node:
                return last_node
            last_node = traverse(curr_node.left, last_node, curr_count, max_count, modes)
            if last_node and last_node.val == curr_node.val:
                curr_count[0] += 1
            else:
                curr_count[0] = 1
            if curr_count[0] > max_count[0]:
                max_count[0] = curr_count[0]
                del modes[:]  # Clear without reset the list, otherwise modes will be lost.
                modes.append(curr_node.val)
            elif curr_count[0] == max_count[0]:
                modes.append(curr_node.val)
            return traverse(curr_node.right, curr_node, curr_count, max_count, modes)
            
        curr_count, max_count, modes = [0], [0], []
        last_node = traverse(root, None, curr_count, max_count, modes)
        return modes

