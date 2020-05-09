from common import TreeNode

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        def traverse(root, nodes, h_level, v_level, counter):
            if not root:
                return counter
            
            nodes.append((h_level, v_level, counter, root.val))
            counter = traverse(root.left, nodes, h_level-1, v_level+1, counter+1)
            counter = traverse(root.right, nodes, h_level+1, v_level+1, counter+1)
            return counter

        nodes = []
        traverse(root, nodes, 0, 0, 0)
        nodes = sorted(nodes)
        h_prev = None
        result = []
        for h, _, _, val in nodes:
            if h != h_prev:
                result.append([val])
                h_prev = h
            else:
                result[-1].append(val)
        return result
