import unittest

from l0167_two_sum_2_input_array_is_sorted import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 2], Solution().twoSum([2, 7, 11, 15], 9))