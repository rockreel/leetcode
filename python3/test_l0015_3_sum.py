import unittest

from l0015_3_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([[-2,0,2]], Solution().threeSum([-2,0,0,2,2]))
