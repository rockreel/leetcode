class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = Node(node.val, [])
        queue = [(node, cloned)]
        visited_map = dict()
        while queue:
            old_node, new_node = queue.pop(0)
            visited_map[old_node] = new_node
            for neighbor in old_node.neighbors:
                if neighbor not in visited_map:
                    new_neighbor = Node(neighbor.val, [])
                    new_node.neighbors.append(new_neighbor)
                    visited_map[neighbor] = new_neighbor
                    queue.append((neighbor, new_neighbor))
                else:
                    new_node.neighbors.append(visited_map[neighbor])

        return cloned