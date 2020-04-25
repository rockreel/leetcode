from common import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        current = root
        stack = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                if node.right:
                    current = node.right

