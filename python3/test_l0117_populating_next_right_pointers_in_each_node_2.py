import unittest

from common import Node
from l0116_populating_next_right_pointers_in_each_node import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        tree = Node(
            1,
            Node(2, Node(4), Node(5)),
            Node(3, None, Node(7))
        )
        Solution().connect(tree)
        self.assertEqual(tree.next, None)
        self.assertEqual(tree.left.next, tree.right)
        self.assertEqual(tree.right.next, None)
        self.assertEqual(tree.left.left.next, tree.left.right)
        self.assertEqual(tree.left.right.next, tree.right.right)
        self.assertEqual(tree.right.right.next, None)
