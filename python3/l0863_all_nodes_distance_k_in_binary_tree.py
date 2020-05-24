from common import TreeNode

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def get_nodes(root: TreeNode, k: int) -> List[TreeNode]:
            # Get nodes in the tree that are k distance from root.
            if not root or k < 0:
                return []
            if k == 0:
                return [root.val]
            
            return get_nodes(root.left, k-1) + get_nodes(root.right, k-1)
        
        def traverse(root: TreeNode, target: TreeNode, k: int, nodes: List[TreeNode]) -> int:
            # Traverse the tree, returns the distance from target to root, if no target is found, return -1.
            # It also adds nodes at k distance to target to nodes list.
            if not root:
                return -1
            if root == target:
                nodes.extend(get_nodes(root, k))
                return 0
            
            left_dist = traverse(root.left, target, k, nodes)
            if left_dist != -1:
                if left_dist == k - 1:
                    nodes.extend(get_nodes(root, 0))

                nodes.extend(get_nodes(root.right, k - left_dist - 2))
                return left_dist + 1
            
            right_dist = traverse(root.right, target, k, nodes)
            if right_dist != -1:
                if right_dist == k - 1:
                    nodes.extend(get_nodes(root, 0))

                nodes.extend(get_nodes(root.left, k - right_dist - 2))
                return right_dist + 1
            return -1
        
        nodes = []
        traverse(root, target, K, nodes)
        return nodes
