import unittest

from l1631_path_with_minimum_effort import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
        self.assertEqual(1, Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
        self.assertEqual(0, Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
