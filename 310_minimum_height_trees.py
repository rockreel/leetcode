# Peel onion.
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 3:
            return range(n)
            
        from collections import defaultdict
        nodes = set(range(n))
        node_map = defaultdict(set)
        for e in edges:
            node_map[e[0]].add(e[1])
            node_map[e[1]].add(e[0])
        queue = [(n, next(iter(node_map[n]))) for n in node_map if len(node_map[n])==1]
        nodes.difference_update([n for n, _ in queue])
                
        while len(nodes) > 2:
            new_queue = []
            for node, neighbour in queue:
                node_map[neighbour].remove(node)
                if len(node_map[neighbour]) == 1:
                    new_queue.append((neighbour, next(iter(node_map[neighbour]))))
                    nodes.remove(neighbour)
            queue = new_queue
        return list(nodes)

# Brutal force find height for every tree.
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def height(root, node_map):
            # BFS to find min height.
            height = 0
            queue = [root, None]
            visited = set()
            i = 0
            while queue:
                node = queue.pop(0)
                if node is not None:
                    visited.add(node)
                    for next_node in node_map[node]:
                        if next_node not in visited:
                            queue.append(next_node)
                else:
                    height +=1
                    if queue:
                        queue.append(None)
                            
            return height

        from collections import defaultdict
        node_map = defaultdict(list)
        for edge in edges:
            node_map[edge[0]].append(edge[1])
            node_map[edge[1]].append(edge[0])
        heights = [0] * n  
        for node in range(n):
            heights[node] = height(node, node_map)
        min_height = min(heights)
        return [i for i, h in enumerate(heights) if h == min_height]

