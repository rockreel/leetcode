import unittest

from l0417_pacific_atlantic_water_flow import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]), 
            sorted(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])))
        self.assertEqual(
            sorted([[0,0],[0,1],[1,0],[1,1]]), 
            sorted(Solution().pacificAtlantic([[2,1],[1,2]])))

        