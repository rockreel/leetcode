import unittest

from l1642_furthest_building_you_can_reach import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7, 
            Solution().furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))
        self.assertEqual(
            4, 
            Solution().furthestBuilding([4,2,7,6,9,14,12], 5, 1))
        self.assertEqual(
            3, 
            Solution().furthestBuilding([14,3,19,3], 17, 0))
