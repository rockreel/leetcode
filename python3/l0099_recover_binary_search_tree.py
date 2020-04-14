from common import TreeNode

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        prev = None
        stack = []
        nodes_to_swap = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    node = stack.pop()
                    if prev and prev.val > node.val:
                        if not nodes_to_swap:
                            nodes_to_swap.append(prev)
                            nodes_to_swap.append(node)
                        else:
                            nodes_to_swap.append(node) 
                    prev = node
                    if node.right:
                        current = node.right
        
        nodes_to_swap[0].val, nodes_to_swap[-1].val = nodes_to_swap[-1].val, nodes_to_swap[0].val 

        return