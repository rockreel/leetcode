import unittest

from l1971_find_if_path_exists_in_graph import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
        self.assertEqual(
            False, 
            Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
