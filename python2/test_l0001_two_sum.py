import unittest

import l0001_two_sum

class TestRestore(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([0, 1], l0001_two_sum.Solution().twoSum([2, 7, 11, 15], 9))