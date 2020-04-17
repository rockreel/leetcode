import unittest

from l0133_clone_graph import Node
from l0133_clone_graph import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        cloned = Solution().cloneGraph(node1)
        self.assertEqual(node1.val, cloned.val)
        self.assertEqual(set([2, 4]), set([n.val for n in cloned.neighbors]))
        self.assertEqual(set([1, 3]), set([n.val for n in cloned.neighbors[0].neighbors]))
        self.assertEqual(set([1, 3]), set([n.val for n in cloned.neighbors[1].neighbors]))