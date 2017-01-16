# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        new_node = UndirectedGraphNode(node.label)
        visited_nodes = set()
        node_map = {node: new_node}
        queue = [node]
        while queue:
            curr_node = queue.pop()
            if curr_node in visited_nodes:
                continue
            else:
                visited_nodes.add(curr_node)
            # Create all it's neighbours and add to neighbor lists of
            # the new node created for it.
            for neighbor in curr_node.neighbors:
                queue.append(neighbor)
                new_neighbor = node_map.get(
                    neighbor, UndirectedGraphNode(neighbor.label))
                node_map[curr_node].neighbors.append(new_neighbor)
                node_map[neighbor] = new_neighbor
            
        return new_node
        

