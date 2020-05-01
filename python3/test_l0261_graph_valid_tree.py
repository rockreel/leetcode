import unittest

from l0261_graph_valid_tree import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertEqual(False, Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))