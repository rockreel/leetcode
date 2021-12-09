import unittest

from l0941_valid_mountain_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            False, 
            Solution().validMountainArray([2, 1]))
        self.assertEqual(
            False, 
            Solution().validMountainArray([3, 5, 5]))
        self.assertEqual(
            False, 
            Solution().validMountainArray([1, 2, 3]))
        self.assertEqual(
            True, 
            Solution().validMountainArray([0, 3, 2, 1]))
        