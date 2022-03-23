from typing import Optional, List
from collections import defaultdict
from common import TreeNode

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node, tree_map):
            if not node:
                return 'null'
            key = '%s,%s,%s' % (node.val, traverse(node.left, tree_map), traverse(node.right, tree_map))
            tree_map[key].append(node)
            return key
                
        tree_map = defaultdict(list)
        traverse(root, tree_map)
        return [v[0] for k, v in tree_map.items() if len(v) > 1]