import unittest

from l0323_number_of_connected_components_in_an_undirected_graph import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))