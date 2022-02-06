import unittest

from l1584_min_cost_to_connect_all_points import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(20, Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
        self.assertEqual(18, Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
