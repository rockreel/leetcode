import unittest

import common
from l0001_two_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([0, 1], Solution().twoSum([2, 7, 11, 15], 9))
