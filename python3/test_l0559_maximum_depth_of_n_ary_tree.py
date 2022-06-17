import unittest

from l0559_maximum_depth_of_n_ary_tree import Node
from l0559_maximum_depth_of_n_ary_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        t1 = Node(1)
        t2 = Node(2)
        t3 = Node(3)
        t4 = Node(4)
        t5 = Node(5)
        t6 = Node(6)
        t1.children = [t3, t2, t4]
        t3.children = [t5, t6]
        self.assertEqual(3, Solution().maxDepth(t1))
