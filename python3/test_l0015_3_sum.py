import unittest

from l0015_3_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted([[-1, -1, 2], [-1, 0, 1]]), sorted(Solution().threeSum([-1, 0, 1, 2, -1, -4])))
        self.assertEqual(sorted([[-2,0,2]]), sorted(Solution().threeSum([-2,0,0,2,2])))
