import unittest

from l0429_nary_tree_level_order_traversal import Solution, Node

class Test(unittest.TestCase):
    
    def test_solution(self):
        root = Node(1, [])
        n3 = Node(3, [])
        n2 = Node(2, [])
        n4 = Node(4, [])
        root.children = [n3, n2, n4]
        n5 = Node(5, [])
        n6 = Node(6, [])
        n3.children = [n5, n6] 
        self.assertEqual(
            [[1],[3,2,4],[5,6]], 
            Solution().levelOrder(root))
