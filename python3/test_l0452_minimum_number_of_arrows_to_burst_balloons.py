import unittest

from l0452_minimum_number_of_arrows_to_burst_balloons import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
        self.assertEqual(4, Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
        self.assertEqual(2, Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
