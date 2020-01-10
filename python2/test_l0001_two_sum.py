import unittest

from l0001_two_sum import Solution

class TestRestore(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([0, 1], Solution().twoSum([2, 7, 11, 15], 9))