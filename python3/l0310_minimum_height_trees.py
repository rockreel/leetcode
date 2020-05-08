from collections import defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(n))
        node_map = defaultdict(list)
        for e in edges:
            node_map[e[0]].append(e[1])
            node_map[e[1]].append(e[0])
        
        # Start with nodes with only one link, gradually remove them
        # until last two nodes left is the tree root.
        queue = [node for node, children in node_map.items() if len(children) == 1]
        
        while len(nodes) > 2:
            nodes.difference_update(queue)
            new_queue = []
            for n in queue:
                for child in node_map[n]:
                    node_map[child].remove(n)
                    if len(node_map[child]) == 1:
                        new_queue.append(child)
            queue = new_queue

        return list(nodes)