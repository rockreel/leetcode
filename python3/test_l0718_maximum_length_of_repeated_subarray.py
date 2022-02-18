import unittest

from l0718_maximum_length_of_repeated_subarray import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))
        self.assertEqual(5, Solution().findLength([0,0,0,0,0], [0,0,0,0,0]))
