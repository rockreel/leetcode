from collections import defaultdict

class Solution:   
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        node_map = defaultdict(list)
        for e in edges:
            node_map[e[0]].append(e[1])
            node_map[e[1]].append(e[0])
        visited = set([0])
        edge_set = set([(e[0], e[1]) for e in edges])
        
        queue = [0]
        while queue:
            node = queue.pop()
            for neighbor in node_map[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    if (node, neighbor) in edge_set:
                        edge_set.remove((node, neighbor))
                    elif (neighbor, node) in edge_set:
                        edge_set.remove((neighbor, node))
        
        # All edges should be visited once, and all nodes are visited.
        return len(edge_set) == 0 and len(visited) == n
