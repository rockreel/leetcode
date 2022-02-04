import unittest

from l0797_all_paths_from_source_to_target import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[0,1,3],[0,2,3]]), 
            sorted(Solution().allPathsSourceTarget([[1,2],[3],[3],[]])))
        self.assertEqual(
            sorted([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]), 
            sorted(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])))
